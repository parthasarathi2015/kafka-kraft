from confluent_kafka import Producer
import json
import os
import random

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL", "kafka-2:9092")
PROD_TOPIC = os.environ.get("PROD_TOPIC", "user-delete")

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] :: message:{msg.value()}")

def send_message(key: str, message):
    producer = Producer({'bootstrap.servers': KAFKA_BROKER_URL})
    message= json.dumps(message).encode('utf-8')
    producer.produce(PROD_TOPIC, key, message, callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    id = random.randrange(1, 10)
    send_message(
        key=f"message_{id}",
        message={"message":{"id": id,"val": f"User id {id} deleted successfully!"}}
    )
