import sys
import pandas as pd 
import psycopg2 as pg 
import requests
import json

def handler(event, context):
    print(event, context)
    body_json = json.loads(event["body"])
    print(":::::json body", body_json)
    resp=None
    if body_json["get_response"] == "200":
        resp = "200"
    elif body_json["get_response"] == "400":
        resp = "400"
    elif body_json["get_response"] == "500":
        resp = "500"
    elif body_json["get_response"] == "401":
        resp = "401"
    elif body_json["get_response"] == "502":
        resp = "502"
    else:
        resp = "501"
    headers = {
            "Access-Control-Allow-Origin": "*",
            "Strict-Transport-Security": "max-age=31536000",
            "X-Frame-Options": "DENY",
            "Content-Security-Policy": "default-src 'none'",
            "X-Content-Type-Options": "nosniff",
            "Content-Type": "application/json",
        }
    return {
        "isBase64Encoded": False,
        "statusCode": int(resp),
        "body": json.dumps({
            "Response code": resp,
            "event" : body_json
        }),
        "headers": headers
    }