import boto3
from botocore.exceptions import ClientError
import os

def get_variable(var_name):
    response = boto3.client("ssm").get_parameter(Name=var_name)
    return response['Parameter']['Value']
    

def store_data(dir, bucket, key):
    
    tmp = '/tmp'
    zip_file = 'my_file'
    try:
        boto3.resource('s3').Object(bucket, key).upload_file(os.path.join(tmp, zip_file))
        message = "Pass"
    except ClientError as ex:
        message = "Fail"
    
    return message    