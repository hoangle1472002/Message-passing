import os
from kafka import KafkaConsumer

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    TOPIC_NAME = 'items'
    consumer = KafkaConsumer(TOPIC_NAME)
    for message in consumer:
        print (message)
    app.run(debug=True)
