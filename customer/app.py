from redis import Redis
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from util.messageUtils import convert_sub_data, convert_pub_data


redis_pubsub = Redis(db=1)

customer_data = {
    "username" : "malex",
    "status" : "active"
}

pubsub = redis_pubsub.pubsub()

pubsub.subscribe("order_channel")

for message in pubsub.listen():
    if message['type'] == "message":
        order_data = convert_sub_data(message)
        order_id = order_data["order_id"]
        print(f"got order by order_id : {order_id}")
        redis_pubsub.publish("cutomer_channel", convert_pub_data(customer_data))
