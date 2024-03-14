import os
from kafka import KafkaProducer

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    TOPIC_NAME = 'items'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    producer.send(TOPIC_NAME, b'Test Message!!!')
    producer.flush()
    app.run(debug=True)
