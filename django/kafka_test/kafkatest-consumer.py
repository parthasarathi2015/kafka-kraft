import os
from confluent_kafka import Consumer, KafkaException


KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL", "kafka-2:9092")
PROD_TOPIC = os.environ.get("PROD_TOPIC", "user-delete")
GROUP_ID = os.environ.get("GROUP_ID", "user-delete-group")
POLL_FREQUENCY = float(os.environ.get("GROUP_ID", 3.0))

def consume_messages():
    consumer = Consumer({
        'bootstrap.servers': KAFKA_BROKER_URL,
        'group.id': GROUP_ID,
        'auto.offset.reset': 'earliest'
    })

    consumer.subscribe([PROD_TOPIC])

    try:
        while True:
            msg = consumer.poll(1.0)  # Timeout in seconds
            if msg is None:
                print("No consumer message..................!")
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break
            print(f"Received message: {msg.value().decode('utf-8')}")
    finally:
        consumer.close()

if __name__ == "__main__":
    print("Messages consumer started ....")
    consume_messages()
