#!/usr/bin/env python 

import os, sys 
from .aws import get_session, list_objects
from .config import get_config
from dateutil import parser



def process_key(key):
        pipeline, logs, segment, month, filename = key.split("/")
        #print(key)
        return (month, filename)

def download(what, month=None, day=None):

    print("Downloading files for", month, " and", day)

    session = get_session(what)
    s3 = session.resource('s3')

    config = get_config()
    workspace = config[what]['workspace']     
    bucket = config[what]['bucket']
    prefix = config[what]['prefix']

    key = None

    if month is not None:
    	prefix = prefix + "/" + month

    	if day is not None:
    		key = prefix + "/" + day + "-CCD.tsv"

    else:
        if day is not None:
            d = parser.parse(day)
            month = str(d.year*100 + d.month)
            prefix = prefix + "/" + month
            key = prefix + "/" + day + "-CCD.tsv"

    if key is not None:
        (month, filename) = process_key(key)
        localpath = os.path.join(workspace, month, filename)
        if not os.path.exists(os.path.dirname(localpath)):
            os.makedirs(os.path.dirname(localpath))
        result = s3.meta.client.download_file(bucket, key, localpath)
        print(key, "===>", localpath)

    else:
            objs = s3.Bucket(bucket).objects.filter(Prefix=prefix)

            for obj in objs:
                key = obj.key
                if not key.endswith(".tsv"):
                    continue
                (month, filename) = process_key(key)
                localpath = os.path.join(workspace, month, filename)
                if not os.path.exists(os.path.dirname(localpath)):
                    os.makedirs(os.path.dirname(localpath))
                result = s3.meta.client.download_file(bucket, key, localpath)
                print(key, "===>", localpath)

    print("Please find downloaded files in {}".format(workspace))			











    









