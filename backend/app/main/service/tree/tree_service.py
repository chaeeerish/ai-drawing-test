# standard library imports
import io
# Third party imports
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# local application imports
from main.model.domain.user.user_model import *
from main.model.repository.user.user_repository import *
from main.service.common import *
from main.service.tree.tree_result import *
from main.service.tree.tree_service import *
from main.service.character.character import *

TOTAL_GENTLE = 7
TOTAL_CONFIDENCE = 10
TOTAL_HAPPINESS = 10
TOTAL_SOCIAL_CONFIENDCE = 10
TOTAL_HIGH_ESTEEM = 8

class Result:
    size = ''
    type = ''
    leap = ''
    branch = ''
    stem = ''
    root = ''
    figures = [0, 0, 0, 0, 0]
    figures_gen = 0.0
    figures_con = 0.0
    figures_hap = 0.0
    figures_soc = 0.0
    figures_hig = 0.0
    character = -1

    def __init__(self):
        pass

def call_tree_model(id):
    # 초기화
    user = find_user(id=id)
    result = Result()
    
    size_result_list = []
    type_result_list = []
    leap_result_list = []
    branch_result_list = []
    stem_result_list = []
    root_result_list = []
    
    # 0. tree_size_location
    size_result_list, crop_img_dict = detection_tree(user.tree_image)

    # 1.0, 1001: 가지, 잎 tree crop leaf branch
    # 2.0, 1002: 줄기 tree crop stem
    # 3.0, 1003: 뿌리 tree crop root
    # 4.0, 1004: 나무 전체 tree crop type

    # 1. tree_type 나무 타입 분류 모델
    # return 0 1 2 3 4 중에 하나 
    if check_model_execution_conditions(crop_img_dict[4.0]):
        type_result_list.append(classification('tree_type', crop_img_dict[4.0], 300))
    else:
        # error 발생시키기
        pass

    # 2. 3. 잎, 열매, 꽃, 가지  
    if check_model_execution_conditions(crop_img_dict[1.0]):
        label_names = [TREE_LEAF_FRUIT.summary, TREE_BRANCH_UP.summary, TREE_LEAF_LEAFY.summary, TREE_LEAF_FLOWER.summary, TREE_BRANCH_NET.summary, TREE_LEAF_BIG.summary, TREE_BRANCH_UNCLOSED.summary]
        label_return = classification_multi('leaf_branch', crop_img_dict[1.0], label_names, 200, 7)
        
        for leaf in TREE_LEAF_RESULT:
            if leaf.summary in label_return:
                leap_result_list.append(leaf.index)
    
        for branch in TREE_BRANCH_RESULT:
            if branch.summary in label_return:
                branch_result_list.append(branch.index)

    # 4. stem 줄기 => [0, 0, 0]
    if check_model_execution_conditions(crop_img_dict[2.0]):
        label_names = [TREE_STEM_RING.summary, TREE_STEM_ANIMAL.summary, '나이테_나무껍질_옹이_X']
        label_return = classification_multi('stem', crop_img_dict[2.0], label_names, 200, 3)

        for stem in TREE_STEM_RESULT:
            if stem.summary in label_return:
                stem_result_list.append(stem.index)
        
    # 5. root 뿌리 => 1 2 3 4 5 중에 하나
    if check_model_execution_conditions(crop_img_dict[3.0]):
        root_result_list.append(classification('root', crop_img_dict[3.0], 300))

    # result save
    result.size = ''.join(map(str, size_result_list))
    result.type = ''.join(map(str, type_result_list))
    result.leap = ''.join(map(str, leap_result_list))
    result.branch = ''.join(map(str, branch_result_list))
    result.stem = ''.join(map(str, stem_result_list))
    result.root = ''.join(map(str, root_result_list))
    
    # caculate figures
    result.figures = calculate_figures(TREE_SIZE_RESULT, size_result_list, result.figures)
    result.figures = calculate_figures(TREE_TYPE_RESULT, type_result_list, result.figures)
    result.figures = calculate_figures(TREE_LEAF_RESULT, leap_result_list, result.figures)
    result.figures = calculate_figures(TREE_BRANCH_RESULT, branch_result_list, result.figures)
    result.figures = calculate_figures(TREE_STEM_RESULT, stem_result_list, result.figures)
    result.figures = calculate_figures(TREE_ROOT_RESULT, root_result_list, result.figures)
    
    # figures/total
    result.figures_gen = round(1 - (result.figures[0] / TOTAL_GENTLE), 4)
    result.figures_con = round(1 - (result.figures[1] / TOTAL_CONFIDENCE), 4)
    result.figures_hap = round(1 - (result.figures[2] / TOTAL_HAPPINESS), 4)
    result.figures_soc = round(1 - (result.figures[3] / TOTAL_SOCIAL_CONFIENDCE), 4)
    result.figures_hig = round(1 - (result.figures[4] / TOTAL_HIGH_ESTEEM), 4)
    
    # match character
    result.character = match_character([result.figures_gen, result.figures_con, result.figures_hap, result.figures_soc, result.figures_hig])
    
    save_user_tree_result(id=id, result_cls=result)

def check_model_execution_conditions(img):
    if img is not None:
        return True
    return False

#detection function
def detection_tree(img_binary):
    result_list = []
    
    encoded_img = np.fromstring(img_binary, dtype = np.uint8)
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
    
    img_array = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB) #이미지를 읽고 rgb로 변환한다. (opencv는 bgr로 읽음)
    img_tensor = tf.convert_to_tensor(img_array, dtype=tf.uint8)[tf.newaxis, ...] #텐서 형식으로 변환
    
    height = img_array.shape[0]
    width = img_array.shape[1]

    draw_img = img_array.copy()

    model = get_detection_model('saved_model')

    #사용자 이미지 추론 (detection)
    result = model(img_tensor)
    result = {key:value.numpy() for key,value in result.items()}
    
    #임계값 지정. 50% 이상일 때만 바운딩박스 그림
    SCORE_THRESHOLD = 0.5
    OBJECT_DEFAULT_COUNT = 4 #클래스 개수

    #클래스 매칭
    labels_to_names = {1.0:'1001', 2.0:'1002', 3.0:'1003', 4.0:'1004'}
    
    # 선언
    tree_height = 0
    tree_width = 0
    
    stem_height = 0
    stem_width = 0

    crop_img_dict = {1.0: None, 2.0: None, 3.0: None, 4.0: None}

    for i in range(min(result['detection_scores'][0].shape[0], OBJECT_DEFAULT_COUNT)):
        score = result['detection_scores'][0,i]
        if score < SCORE_THRESHOLD: #임계값보다 작을 경우 break
            break
        box = result['detection_boxes'][0,i]
        left = box[1] * width
        top = box[0] * height
        right = box[3] * width
        bottom = box[2] * height
        class_id = result['detection_classes'][0, i]

        crop_img = draw_img[int(top):int(bottom),int(left):int(right)] #detection 하여 그린 박스만큼 이미지 크롭
        
        # 1.0, 1001: 가지, 잎
        # 2.0, 1002: 줄기
        # 3.0, 1003: 뿌리
        # 4.0, 1004: 나무 전체

        if labels_to_names[class_id] == '1004':
            tree_height = bottom-top
            tree_width = right-left
            result_list.extend(tree_size_loc(height, width, top, bottom, left, right))
        elif labels_to_names[class_id] == '1002':
            stem_height = bottom-top
            stem_width = right-left

        npImage = Image.fromarray(crop_img)
        img_byte_arr = io.BytesIO()
        npImage.save(img_byte_arr, format='jpeg')
        img_byte_arr = img_byte_arr.getvalue()

        # crop한 이미지 db에 저장한다.
        crop_img_dict[class_id] = img_byte_arr
        # update_user_tree_crop(class_id, userid ,img_byte_arr)

        caption = "{}: {:.4f}".format(labels_to_names[class_id], score)
    
    ################
    # 줄기 사이즈
    # stem_size = 0 # 보통이다
    if stem_height < tree_height * (1/6):
        result_list.append(4)

    return result_list, crop_img_dict


def tree_size_loc(height, width, top, bottom, left, right):##새로 생성
    treesizeResult = []
    img_size = height*width
    tree_size = (bottom-top)*(right-left) #트리 크기
    img_center = width / 2 ##그림 중앙 좌표
    tree_center = left + ((right-left)/2) #트리 중앙 좌표

    if tree_size < img_size / 4:
        treesizeResult.append(0)

    if tree_center < img_center / 2:
        treesizeResult.append(1)
    elif tree_center > img_center * 1.5:
        treesizeResult.append(3)
    else:
        treesizeResult.append(2)
        
    return treesizeResult
