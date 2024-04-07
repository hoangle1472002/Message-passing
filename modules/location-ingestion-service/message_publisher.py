import json
import logging
import os

from kafka import KafkaProducer


TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
CLIENT_USERNAME = os.environ["CLIENT_USERNAME"]
CLIENT_PASSWORD = os.environ["CLIENT_PASSWORD"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingestion-service")

config = "security.protocol=SASL_PLAINTEXT sasl.mechanism=SCRAM-SHA-256 sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required username= \"user1\" password=\"8CZxWW2lsk\";"

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

sasl_jaas_config = f'org.apache.kafka.common.security.scram.ScramLoginModule required username="{CLIENT_USERNAME}" password="{CLIENT_PASSWORD}";'
producer.config['broker_list'] = ["udaconnect-kafka-controller-0.udaconnect-kafka-controller-headless.default.svc.cluster.local:9092"]
producer.config['security.protocol'] = 'SASL_PLAINTEXT'
producer.config['sasl.mechanism'] = 'SCRAM-SHA-256'
producer.config['sasl.jaas.config'] = 'org.apache.kafka.common.security.scram.ScramLoginModule required username="user1" password="8CZxWW2lsk";'


def publish_location(location_data):
    print(f"Data to be sent to kafka: {location_data}")
    encoded_data = json.dumps(location_data).encode('utf-8')
    print(f"Data to be sent to kafka: {encoded_data}")
    producer.send(TOPIC_NAME, encoded_data)
    producer.flush()
    logger.info(f"Published location data {location_data} to kafka successfully.")