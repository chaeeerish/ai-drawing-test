# standard library imports

# Third party imports
import tensorflow as tf
import numpy as np
import cv2

# local application imports
from main.model.domain.user.user_model import *
from main.model.repository.user.user_repository import *
from main.service.house.house_result import *
from main.service.common import *

class UserHouseResult:
    type = ''
    roof = ''
    door = ''
    window = ''

    def __init__(self):
        pass

def house_process(id):
    # 초기화
    user = find_user(id)
    img_binary = user.house_image
    result = UserHouseResult()

    total_result_dict = detection_house(img_binary)

    type_result_list = []
    type_result_list.append(classification('house', img_binary, 150))
    
    # result
    result.roof = ''.join(map(str, total_result_dict["roof_result"]))
    result.door = ''.join(map(str, total_result_dict["door_result"]))
    result.window = ''.join(map(str, total_result_dict["window_result"]))
    result.type = ''.join(map(str, type_result_list))
    save_user_house_result(id=id, result_cls=result)

def detection_house(binaryimg):
    roof_result_list=[]
    door_result_list=[]
    window_result_list=[]

    encoded_img = np.fromstring(binaryimg, dtype = np.uint8)
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    img_array = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB) #이미지를 읽고 rgb로 변환한다. (opencv는 bgr로 읽음)
    img_tensor = tf.convert_to_tensor(img_array, dtype=tf.uint8)[tf.newaxis, ...] #텐서 형식으로 변환
    
    height = img_array.shape[0]
    width = img_array.shape[1]

    draw_img = img_array.copy()

    # 모델 로드
    model = get_detection_model('saved_model2')

    # 사용자 이미지 추론 (detection)
    result = model(img_tensor)
    result = {key:value.numpy() for key,value in result.items()}
    
    # 임계값 지정. 이상일 때만 바운딩박스 그림
    SCORE_THRESHOLD = 0.7
    OBJECT_DEFAULT_COUNT = 25 #클래스 개수

    # 클래스 매칭
    labels_to_names = {1.0:'1001', 2.0:'1002', 3.0:'1003', 4.0:'1004'}
    
    detection_list = []
 
    roof_score_list = []
    roof_width_list = [] 
    roof_height_list = []
    
    wall_score_list = []
    wall_list = []
    wall_width_list=[]
    wall_height_list=[]

    window_list = [] 
    window_width_list = []
    window_height_list = []

    door_score_list = []
    door_list = []
    door_width_list = []
    door_height_list = []
    
    # 1001: 지붕
    # 1002: 벽
    # 1003: 창문
    # 1004: 문

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
        
        if labels_to_names[class_id] == '1001': # 지붕
          roof_width = right - left
          roof_height = bottom - top
          roof_score_list.append(score)
          roof_width_list.append(roof_width)
          roof_height_list.append(roof_height)

        elif labels_to_names[class_id] == '1002': # 벽
          wall_left = left
          wall_right = right
          wall_height = bottom - top
          wall_width = right - left
          wall_score_list.append(score)
          wall_width_list.append(wall_width)
          wall_height_list.append(wall_height)
          wall_list.append([wall_left, wall_right, wall_height, wall_width])
        
        elif labels_to_names[class_id] == '1003': # 창문
          window_height = bottom - top
          window_width = right - left
          window_width_list.append(window_width)
          window_height_list.append(window_height)
          window_list.append([window_height, window_width])
          
        elif labels_to_names[class_id] == '1004': # 문
          door_left = left
          door_right = right
          door_height = bottom - top
          door_width = right - left
          door_score_list.append(score)
          door_list.append([door_left, door_right, door_height, door_width])
          door_width_list.append(door_width)
          door_height_list.append(door_height)
        
        detection_list.append(labels_to_names[class_id])
        caption = "{}: {:.4f}".format(labels_to_names[class_id], score)

    # 1001: 지붕 Roof
    # 지붕 크기
    if detection_list.count('1001') == 0: # 지붕 없다
       roof_result_list.append(0)
    else: # 지붕 있다
       if detection_list.count('1002') >= 1: # 벽 있다
        wall_score_max_index = wall_score_list.index(max(wall_score_list))
        wall_width = wall_width_list[wall_score_max_index]
        wall_height = wall_height_list[wall_score_max_index]

        if detection_list.count('1001') == 1: # 지붕 벽 각각 하나
          roof_width = roof_width_list[0]
          roof_height = roof_height_list[0]
          
          if roof_size(roof_width, wall_width, roof_height, wall_height) == 1 and 1 not in roof_result_list:
            roof_result_list.append(1)
          
        elif detection_list.count('1001') >= 2:
          # max size
          roof_width = max(roof_width_list)
          roof_height = max(roof_height_list)
          if roof_size(roof_width, wall_width, roof_height, wall_height) == 1 and 1 not in roof_result_list:
            roof_result_list.append(1)

          # score
          roof_score_max_index = roof_score_list.index(max(roof_score_list))
          roof_width = roof_width_list[roof_score_max_index]
          roof_height = roof_height_list[roof_score_max_index]
          
          if roof_size(roof_width, wall_width, roof_height, wall_height) == 1 and 1 not in roof_result_list:
            roof_result_list.append(1)

    # 1003: 창문 Window
    # 창문 개수
    if detection_list.count('1003') >= 2: # 창문 2개 이상
        window_result_list.append(1)
    elif detection_list.count('1003') == 0:
        window_result_list.append(0)

    # 창문 크기
    # (창문과 벽이 한 개라도 있으면)
    if detection_list.count('1003') >= 1 and detection_list.count('1002') >= 1:
        window_size_result = window_size(max(window_height_list), max(window_width_list), max(wall_height_list), max(wall_width_list))
        if window_size_result == 1: # 작다
           window_result_list.append(3)
        elif window_size_result == 2: # 크다
           window_result_list.append(2)

    # 1004: 문 Door
    # 문 개수
    if detection_list.count('1004') == 0:
       door_result_list.append(0)

    # 문 위치
    if detection_list.count('1002') == 1 and detection_list.count('1004') == 1: # 문, 벽이 한 개라면
        door_edge_result = door_edge(door_width, wall_width, door_left, door_right, wall_left, wall_right)
        if door_edge_result == 1 or door_edge_result == 2:
            door_result_list.append(5) # 가장자리 함수

    # 문 크기
    if detection_list.count('1004') >= 1 and detection_list.count('1002') >= 1:
      wall_score_max_index = wall_score_list.index(max(wall_score_list))
      wall_width = wall_width_list[wall_score_max_index]
      wall_height = wall_height_list[wall_score_max_index]

      door_score_max_index = door_score_list.index(max(door_score_list))
      door_width = door_width_list[door_score_max_index]
      door_height = door_height_list[door_score_max_index]

      door_size_result = door_size(door_height, door_width, wall_height, wall_width)
      if door_size_result != -1:
        door_result_list.append(door_size_result)

    return {
        "roof_result": roof_result_list,
        "door_result": door_result_list,
        "window_result": window_result_list,
    }

# 지붕이 큰가? 함수
def roof_size(roof_width, wall_width, roof_height, wall_height):
  roof_size = 0
  if int(roof_width) > int(wall_width) * 1.9:
    roof_size = 1 # 크다
  if int(roof_height) > int(wall_height) * 2:
    roof_size = 1
  return roof_size

# 문이 큰가? 함수
def door_size(door_height, door_width, wall_height, wall_width):
  door_size = -1 # 보통
  if door_height > wall_height * (4/5):
    if door_width > wall_width * (3/5):
      door_size = 2 # 넓은
    else:
      door_size = 1 # 큰 (길이)
  elif door_height < wall_height * (1/5):
    if door_width < wall_width * (1/4):
      door_size = 4 # 작은
    else:
      door_size = 3 # 낮은 (길이)
  return door_size

# 문 가장자리 함수
def door_edge(door_width, wall_width, door_left, door_right, wall_left, wall_right):
  door_edge = 0 # 치우치지 않은
  if door_left <= wall_left + (wall_width * (1/4)):
    if door_right <=wall_left + (wall_width * (1/2)):
      door_edge = 1 # 왼쪽 가장자리로 치우친
  elif door_left >= wall_left + (wall_width / 2):
    if door_right >= wall_right - (wall_width / 4):
      door_edge = 2 # 오른쪽 가장자리로 치우친
  return door_edge

# 창문 크기 함수
def window_size(window_height, window_width, wall_height, wall_width):
  window_size = 0 # 보통
  if window_width < wall_width / 6:
    window_size = 1 # 좁은. 작다.
  elif window_width >= wall_width / 2:
    if window_height >= wall_height * 0.8:
      window_size = 2 # 큰 창문 (통유리창 정도)
  return window_size
