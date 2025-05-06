from google.cloud import pubsub_v1
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="pubsub_sim/.env")

PROJECT_ID = os.getenv("GCP_PROJECT_ID")

# Path to service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/aletia/projects/freightflow-dbt/pubsub_sim/keys/service-account.json"

subscription_id = "freight-sub"

# Initialize subscriber
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, subscription_id)


def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()

# Start streaming
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening on {subscription_path}...")

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
