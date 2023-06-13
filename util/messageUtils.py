import base64
import json

def convert_sub_data(data):
    return json.loads(base64.b64decode(data).decode('utf-8'))

def convert_pub_data(data):
    return base64.b64encode(json.dumps(data).encode('ascii'))
