import boto3
import os
# from dotenv import load_dotenv

# # .env 파일 로드
# load_dotenv()

# print("******************")
# print(os.environ.get('AWS_ACCESS_KEY_ID'))
# print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
# print("******************")

s3 = boto3.client('s3',
    		aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
            	aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'))
bucket_name = 'ai-drawing-test'

response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    print(f"Bucket: {bucket_name}")
    print("Files:")
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print(f"No files found in the bucket: {bucket_name}")
