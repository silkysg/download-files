#!/usr/bin/env python 

import os, sys
import boto3 
from .config import get_config 

def get_session(what):
    config = get_config() 
    access = config[what]['access']
    secret = config[what]['secret']
    session = boto3.Session(aws_access_key_id=access,
                            aws_secret_access_key=secret,
                            region_name='us-east-1')

    return session


def list_objects(s3, bucket, prefix, maxkeys=1000): 
    objs = s3.meta.client.list_objects(Bucket=bucket,
                                       Prefix=prefix,
                                       Delimiter="/",
                                       MaxKeys=maxkeys
                                   )
    return objs 
