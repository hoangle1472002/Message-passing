import os

from kafka import KafkaConsumer
from location_repository import save_location

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
CLIENT_USERNAME = os.environ["CLIENT_USERNAME"]
CLIENT_PASSWORD = os.environ["CLIENT_PASSWORD"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

sasl_jaas_config = f'org.apache.kafka.common.security.scram.ScramLoginModule required username="{CLIENT_USERNAME}" password="{CLIENT_PASSWORD}";'

consumer.config['security.protocol'] = 'SASL_PLAINTEXT'
consumer.config['sasl.mechanism'] = 'SCRAM-SHA-256'
consumer.config['sasl.jaas.config'] = sasl_jaas_config

while True:
    for message in consumer:
        location_data = message.value.decode('utf-8')
        save_location(location_data)
        