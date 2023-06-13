from redis import Redis
from rq import Queue
from time import sleep
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from util.messageUtils import convert_pub_data
from job import send_order

redis_pubsub = Redis(decode_responses=True , db=1)
redis_queue = Redis(decode_responses=True , db=0)

queue = Queue(connection=redis_queue)

order = {
    "order_id": "22222",
    "product": [
        {
            "name": "hat",
            "code": 111
        },
        {
            "name": "tie",
            "code": 123
        }
    ]
}

order.update({"event_type": "order_created"})
 
complete = False

while complete is False:
    redis_pubsub.publish("order_channel",  convert_pub_data(order))
    job = queue.enqueue(send_order(), job_timeout=10)
    for _ in range(60):
        print(f"job try : {_}")
        if job.result is not None:
            complete = True
            print(job.result)
            break
        sleep(10)




