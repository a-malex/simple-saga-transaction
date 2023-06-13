from redis import Redis
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from util.messageUtils import convert_sub_data

redis = Redis(decode_responses=True, db=1)

def send_order():

    pubsub = redis.pubsub()
    pubsub.subscribe('customer_channel')

    for message in pubsub.listen():
        print(message)
        if message['type'] == 'message':
            customer_data = convert_sub_data(message)
            print(f"received customer data : {customer_data}")
            return customer_data["username"]

