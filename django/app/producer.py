
from kafka import KafkaProducer, KafkaConsumer
import json
import threading

# Kafka Configuration
KAFKA_BROKER = 'kafka-4:9092'
TOPIC_NAME = 'new-test-topic'

def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def create_consumer():
    return KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

def producer_function():
    producer = create_producer()
    for i in range(10):
        message = {"id": i, "data": f"Message {i}"}
        producer.send(TOPIC_NAME, value=message)
        print(f"Produced: {message}")
    producer.flush()

def consumer_function():
    consumer = create_consumer()
    print(f"Consumer type:{repr(type(consumer))}")
    try:
        if consumer:
            for message in consumer:
                if message:
                      print(f"Consumed: {(json.loads(message))}")
                else:
                    print(f"Consumed: not found")
    except Exception as e:
        print(f"e:{repr(e)}")

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer_function)
    consumer_thread = threading.Thread(target=consumer_function, daemon=True)
    
    producer_thread.start()
    # import time
    # time.sleep(100)
    consumer_thread.start()
    
    producer_thread.join()


########################################################
# from kafka import KafkaProducer, KafkaConsumer
# import json
# import logging

# logger = logging.getLogger(__name__)

# logger.error(" logg started...")

# BOOTSTRAP_SERVER = "kafka-4:9092"
# logger.error("message...")
# producer = KafkaProducer(
#     bootstrap_servers=BOOTSTRAP_SERVER,
#     value_serializer=lambda v: json.dumps(v).encode("utf-8"),
# )


# consumer = KafkaConsumer(
#     "new-test-topic",
#     bootstrap_servers=BOOTSTRAP_SERVER,
#     # value_deserializer=lambda x: json.loads(x.decode("utf-8")),
# )
# consumer.subscribe(['ew-test-topic'])

# def send_message(topic, message):
#     producer.send(topic, message)
#     producer.flush()
#     logger.error("send message method")

# # Example Usage
# if __name__ == "__main__":
#     print("sending message...")
#     try:
#         send_message("new-test-topic", "test-message") #{"message": "Hello from Django Producer!"})
#     except Exception as e:
#         logger.error(f"Error sending message: {repr(e)}")

#     logger.error("nessage sent *********")

#     print("Listening for messages...")
#     for message in consumer:
#         print(f"Received: {repr(message)}")

    
#     logger.error("message receving process completed")