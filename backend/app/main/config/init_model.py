import tensorflow as tf
from efficientnet.keras import EfficientNetB3
from keras.models import Model
from tensorflow import keras
import boto3
import botocore
import os
# from dotenv import load_dotenv

# .env 파일 로드
# load_dotenv()

# print("******************")
# print(os.environ.get('AWS_ACCESS_KEY_ID'))
# print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
# print("******************")

# AWS S3 클라이언트 생성
s3 = boto3.client('s3',
                  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                  aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                  )

# S3에서 모델 파일을 로컬로 다운로드하는 함수
def download_s3_model(bucket_name, s3_key, local_path):
    s3.download_file(bucket_name, s3_key, local_path)

# AWS S3 버킷 이름
bucket_name = 'ai-drawing-test'

# detection
model_files = {
    'saved_model/fingerprint.pb': {
        's3_key': 'ml_models/detection/saved_model/fingerprint.pb',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model', 'fingerprint.pb') 
    },
    'saved_model/saved_model.pb': {
        's3_key': 'ml_models/detection/saved_model/saved_model.pb',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model', 'saved_model.pb') 
    },
    'saved_model/variables/variables.data-00000-of-00001': {
        's3_key': 'ml_models/detection/saved_model/variables/variables.data-00000-of-00001',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model', 'variables', 'variables.data-00000-of-00001') 
    },
    'saved_model/variables/variables.index': {
        's3_key': 'ml_models/detection/saved_model/variables/variables.index',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model', 'variables', 'variables.index') 
    },        
    'saved_model2/fingerprint.pb': {
        's3_key': 'ml_models/detection/saved_model2/fingerprint.pb',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model2', 'fingerprint.pb') 
    },
    'saved_model2/saved_model.pb': {
        's3_key': 'ml_models/detection/saved_model2/saved_model.pb',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model2', 'saved_model.pb') 
    },
    'saved_model2/variables/variables.data-00000-of-00001': {
        's3_key': 'ml_models/detection/saved_model2/variables/variables.data-00000-of-00001',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model2', 'variables', 'variables.data-00000-of-00001') 
    },
    'saved_model2/variables/variables.index': {
        's3_key': 'ml_models/detection/saved_model2/variables/variables.index',
        'local_path': os.path.join('ml_models', 'detection', 'saved_model2', 'variables', 'variables.index') 
    },
    'leaf_branch': {
        's3_key': 'ml_models/classification/leaf_branch.h5',
        'local_path': os.path.join('ml_models', 'classification', 'leaf_branch.h5') 
    },
    'tree_type': {
        's3_key': 'ml_models/classification/tree_type.h5',
        'local_path': os.path.join('ml_models', 'classification', 'tree_type.h5') 
    },
    'root': {
        's3_key': 'ml_models/classification/root.h5',
        'local_path': os.path.join('ml_models', 'classification', 'root.h5') 
    },
    'stem': {
        's3_key': 'ml_models/classification/stem.h5',
        'local_path': os.path.join('ml_models', 'classification', 'stem.h5') 
    },
    'house': {
        's3_key': 'ml_models/classification/house.h5',
        'local_path': os.path.join('ml_models', 'classification', 'house.h5')
    }
}

for model_name, model_info in model_files.items():
    try:
        s3_key = model_info['s3_key']
        local_path = model_info['local_path']
        if os.path.isfile(local_path) == False:
            download_s3_model(bucket_name, s3_key, local_path)
                
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f'The file {s3_key} does not exist in S3.')
        else:
            raise

# 전역 변수
model_dict = {
    "saved_model": tf.saved_model.load('ml_models/detection/saved_model'),
    "saved_model2": tf.saved_model.load('ml_models/detection/saved_model2'),
    "leaf_branch": tf.keras.models.load_model('ml_models/classification/leaf_branch.h5'),
    "tree_type": tf.keras.models.load_model('ml_models/classification/tree_type.h5'),
    "root": tf.keras.models.load_model('ml_models/classification/root.h5'),
    "stem": tf.keras.models.load_model('ml_models/classification/stem.h5'),
    "house": tf.keras.models.load_model('ml_models/classification/house.h5'),
    }