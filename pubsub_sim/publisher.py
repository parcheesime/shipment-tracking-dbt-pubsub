from google.cloud import pubsub_v1
import json
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="pubsub_sim/.env")

PROJECT_ID = os.getenv("GCP_PROJECT_ID")

# Path to service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/aletia/projects/freightflow-dbt/pubsub_sim/keys/service-account.json"

# Set project ID and topic ID
topic_id = "freight-updates"

# Initialize publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, topic_id)

# Sample message
message_data = {
    "shipment_id": "feb156c6-788a-4a95",
    "status_update": "in transit",
    "last_known_location": "Phoenix, AZ"
}
data = json.dumps(message_data).encode("utf-8")

# Publish message
future = publisher.publish(topic_path, data)
print(f"Published message ID: {future.result()}")
