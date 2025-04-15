# lab7_script2.py

import logging
import boto3
from botocore.exceptions import ClientError
import requests
import os

s3 = boto3.client('s3', region_name='us-east-1')

# pull file

def download_file(url, file_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
            print(f"File downloaded to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading: {e}")

image_url = 'https://upload.wikimedia.org/wikipedia/commons/a/ae/University_of_Virginia_Rotunda_2006.jpg'
file = 'rotunda.jpg'
path = os.path.join(os.getcwd(), file)

download_file(image_url, path)

# upload to bucket 

bucket = 'ds2002-ybm4rn'

resp = s3.put_object(
    Body = open(file, 'rb'), 
    Bucket = bucket, 
    Key = file, 
)

# presigned url

def create_presigned_url(bucket, file, expiration=60):

    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': file},
            ExpiresIn=expiration,
        )
    except ClientError as e:
        logging.error(e)
        return None 
    # output presigned URL 
    return response

