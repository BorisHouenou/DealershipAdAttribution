import os
import json
import boto3
import requests

S3_BUCKET = os.environ["LANDING_BUCKET"]
FB_TOKEN = os.environ["FB_ACCESS_TOKEN"]
FB_AD_ACCOUNT = os.environ["FB_AD_ACCOUNT_ID"]

s3 = boto3.client("s3")

def lambda_handler(event, context):
    url = f"https://graph.facebook.com/v15.0/{FB_AD_ACCOUNT}/insights"
    params = {
        "access_token": FB_TOKEN,
        "fields": "campaign_name,impressions,clicks,spend,ad_id,date_start,date_stop"
    }
    resp = requests.get(url, params=params)
    data = resp.json().get("data", [])
    key = f"facebook/{context.aws_request_id}.json"
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=json.dumps(data))
    return {"statusCode": 200, "body": json.dumps({'uploaded': key})}
