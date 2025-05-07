from kafka import KafkaConsumer
import json

BOOTSTRAP_SERVER = "kafka-4:9092"
consumer = KafkaConsumer(
    "new-test-topic",
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print("Listening for messages...")
for message in consumer:
    print(f"Received: {message.value}")
