import pandas as pd
import random
from faker import Faker
from datetime import timedelta
import os
import csv

# Initialize
fake = Faker()
random.seed(42)
Faker.seed(42)

# File paths
SHIPMENT_PATH = "freight_data/freight_shipments.csv"
TRACKING_PATH = "freight_data/freight_tracking.csv"

# Load shipments
df = pd.read_csv(SHIPMENT_PATH, parse_dates=["pickup_time"])
tracking_records = []

# Statuses and possible cities
status_updates = ["in transit", "arrived at hub", "delayed", "out for delivery", "delivered"]
locations = [
    "Phoenix, AZ", "Denver, CO", "Las Vegas, NV", "Tucson, AZ",
    "El Paso, TX", "Oklahoma City, OK", "Salt Lake City, UT"
]

# Generate 2–3 updates per shipment
for _, row in df.iterrows():
    shipment_id = row["shipment_id"]
    pickup_time = row["pickup_time"]
    for _ in range(random.randint(2, 3)):
        update_time = pickup_time + timedelta(hours=random.randint(4, 72))
        tracking_records.append({
            "shipment_id": shipment_id,
            "last_known_location": random.choice(locations),
            "last_update_time": update_time.isoformat(),
            "status_update": random.choice(status_updates)
        })

# Write output
os.makedirs("freight_data", exist_ok=True)
with open(TRACKING_PATH, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "shipment_id", "last_known_location", "last_update_time", "status_update"
    ])
    writer.writeheader()
    writer.writerows(tracking_records)

print(f"✅ Tracking data written to {TRACKING_PATH} with {len(tracking_records)} rows.")
