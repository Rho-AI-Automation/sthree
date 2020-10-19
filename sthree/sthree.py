import boto3
import botocore
import os
import tempfile
import json

from sthreehelper import create_config_file

config = create_config_file()

aws_access_key_id= config['aws_key']
aws_secret_access_key= config['aws_secrect']
region_name= config['aws_region']

session = boto3.Session(
    aws_access_key_id= aws_access_key_id,
    aws_secret_access_key= aws_secret_access_key,
    region_name=region_name)

s3 = session.resource('s3')

def return_resource(filename):

    fp = tempfile.TemporaryFile()


    i_filename = filename.replace('s3://','')
    f_split = i_filename.split('/')
    BUCKET_NAME = f_split[0]
    KEY = '/'.join(f for f in f_split[1:])

    bucket = s3.Bucket(BUCKET_NAME)

    tmp = tempfile.NamedTemporaryFile()
    with open (tmp.name,'wb')  as fp:
        bucket.download_fileobj(KEY,fp)
        fp.seek(0)
    fdata = None 
    with open(tmp.name,'r',encoding='utf-8') as f:
        fdata = f.read()
    jdata = json.loads(fdata)
    return jdata 

if __name__ == "__main__":
    fname = 's3://rhoaiautomationindias3/kapowautostorerhoaiindia/google-scrape/10162020/575396.json'
    return_resource(fname)