import os
import json
import boto3

S3_BUCKET = os.environ["LANDING_BUCKET"]

s3 = boto3.client("s3")

def lambda_handler(event, context):
    record = json.loads(event['body'])
    key = f"crm/{context.aws_request_id}.json"
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=json.dumps(record))
    return {'statusCode': 200}
