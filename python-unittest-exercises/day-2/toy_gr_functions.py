import boto3
from botocore.exceptions import ClientError


def remove_iam_user_ssh_public_key_upload(user_name, ssh_pub_key_id):
    
    try:
        response = boto3.client("iam").delete_ssh_public_key(
            UserName=user_name,
            SSHPublicKeyId=ssh_pub_key_id
        )
        message = "success"
    except ClientError as ex:
        message = "fail"
        
    return message    
