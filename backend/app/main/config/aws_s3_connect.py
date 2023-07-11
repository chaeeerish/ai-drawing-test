import boto3
import botocore
import os

bucket_name = os.environ.get('AWS_BUCKET_NAME')

s3 = boto3.resource('s3') 

for bucket in s3.buckets.all(): 
	print(bucket.name)
 
