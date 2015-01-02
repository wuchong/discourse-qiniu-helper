import requests
import logging
import yaml

from qiniu import Auth
from qiniu import BucketManager
from qiniu import build_batch_delete

def list_wrong_files(bucket_name, bucket=None, prefix=None, limit=None):
    if bucket is None:
        bucket = BucketManager(q)
    marker = None
    eof = False
    files_key = []
    while eof is False:
        ret, eof, info = bucket.list(bucket_name, prefix=prefix, marker=marker, limit=limit)
        marker = ret.get('marker', None)
        for item in ret['items']:
            if item['fsize'] == 85:
                files_key.append(item['key'])
    return files_key

def delete_files(bucket_name, files_key, bucket=None):
    if bucket is None:
        bucket = BucketManager(q)
    if len(files_key) == 0:
        logging.info('nothing to delete')
        return
    ops = build_batch_delete(bucket_name,files_key)

    ret,info = bucket.batch(ops)

    if ret[0]['code'] == 200:
        logging.info('delete all success!')
    else:
        logging.error('delete failed!')

def log_init():
    logging.basicConfig(filename = 'qiniu.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s: %(message)s') 
    console = logging.StreamHandler() 
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

log_init()  #log init
config = yaml.load(open('_config.yml'))  #load qiniu access config

access_key = config.get('access_key')
secret_key = config.get('secret_key')
bucket_name = config.get('bucket_name')

q = Auth(access_key,secret_key)
bucket = BucketManager(q)

prefix = "user_avatar/" + config.get('site') + "/"

files_key = list_wrong_files(bucket_name,bucket,prefix)

logging.info('wrong files : ' + str(len(files_key)) )
logging.info(files_key)

delete_files(bucket_name,files_key,bucket)


