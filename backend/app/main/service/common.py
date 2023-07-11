# standard library imports
import json
# Third party imports
import tensorflow as tf
import numpy as np
import cv2
import numpy as np
# local application imports
from main.config.init_model import model_dict

def result_index_to_json(matched_list, matching_list): # db테이블과 찾고자하는 id 값 받고 resultStr에 저장
    result_json = {}

    for char in matching_list:
        index = int(char)
        row = matched_list[index]
        title = row.title
        result = row.result
        result_json[title]=result
    
    return result_json    

def calculate_figures(matched_list, matching_list, score):
    for index in matching_list:
        row = matched_list[index]
        score = [x+y for x,y in zip(score, row.score)]
        
    return score

def get_classfication_model(model_file_name):
    if model_dict[model_file_name] is None:
        model = tf.keras.models.load_model('./model/classification/'+model_file_name+'.h5') #모델 로드
    else:
        model = model_dict[model_file_name]
    return model

def get_detection_model(model_file_name):
    if model_dict[model_file_name] is None:
        model = tf.saved_model.load('./model/detection\\'+model_file_name) #모델 로드
    else: 
        model = model_dict[model_file_name]
    return model

#classification funcation
def classification(model_file_name, binary_img, SIZE):###########수정 내용. 매개변수 SIZE 추가. 이유: 모델 네트워크가 모두 같지 않다면 인풋 사이즈가 달라짐
    model = get_classfication_model(model_file_name)

    encoded_img = np.fromstring(binary_img, dtype = np.uint8)
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    img_array = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB) #아까 잘라서 저장한 나무 전체 이미지 불러온다
    image = cv2.resize(img_array, dsize=(SIZE, SIZE)) #리사이징
    image = np.array(image) #np array type으로 변경
    image = image/255.
    image = np.expand_dims(image, axis=0) #차원 추가
    
    prediction = model.predict(image) #추론
    result = np.argmax(prediction) #결과 확인.
    return result

#######멀티라벨 모델로 갈 경우 사용.
def classification_multi(model_file_name, binary_img, class_li, SIZE, COUNT):
    SCORE_THRESHOLD = 0.3

    model = get_classfication_model(model_file_name)

    encoded_img = np.fromstring(binary_img, dtype = np.uint8)
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

    img_array = cv2.cvtColor(decoded_img, cv2.COLOR_BGR2RGB) #아까 잘라서 저장한 나무 전체 이미지 불러온다
    image = cv2.resize(img_array, dsize=(SIZE, SIZE)) #리사이징
    image = np.array(image) #np array type으로 변경
    image = image/255.
    image = np.expand_dims(image, axis=0) #차원 추가

    proba = model.predict(image)

    sorted_categories = np.argsort(proba[0])[:-(COUNT+1):-1]

    result_list=[]

    for i in range(COUNT):
        if proba[0][sorted_categories[i]] > SCORE_THRESHOLD:
            result_list.append(class_li[sorted_categories[i]])
    return result_list