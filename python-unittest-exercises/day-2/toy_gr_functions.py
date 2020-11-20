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

def enable_s3_public_access_block(bucket_name):
    
    try:
        response = boto3.client("s3").put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": True,
                "IgnorePublicAcls": True,
                "BlockPublicPolicy": True,
                "RestrictPublicBuckets": True,
            }
        )
        message = "success"
    except ClientError as ex:
        message = "fail"
    

def check_public_access_block(bucket_name):
    
    try:
        response = boto3.client("s3").get_public_access_block(Bucket=bucket_name)
        blocked_pub_acl = response["PublicAccessBlockConfiguration"]["BlockPublicAcls"]
        ignore_pub_acls = response["PublicAccessBlockConfiguration"]["IgnorePublicAcls"]
        blocked_pub_pol = response["PublicAccessBlockConfiguration"]["BlockPublicPolicy"]
        restrict_public = response["PublicAccessBlockConfiguration"]["RestrictPublicBuckets"]
        
        return bool(
            blocked_pub_acl and ignore_pub_acls and blocked_pub_pol and restrict_public
        )
    except ClientError as ex:
        return False