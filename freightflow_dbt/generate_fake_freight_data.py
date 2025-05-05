import csv
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()

NUM_RECORDS = 500
OUT_FILE = "freight_data/freight_shipments.csv"

os.makedirs("freight_data", exist_ok=True)

statuses = ["pending", "in_transit", "delivered"]

with open(OUT_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "shipment_id", "origin", "destination",
        "weight_kg", "cost_usd", "pickup_time", "status"
    ])
    
    for _ in range(NUM_RECORDS):
        shipment_id = fake.uuid4()
        origin = f"{fake.city()}, {fake.state_abbr()}"
        destination = f"{fake.city()}, {fake.state_abbr()}"
        weight_kg = random.randint(500, 5000)
        cost_usd = round(random.uniform(200, 5000), 2)
        pickup_time = (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat()
        status = random.choice(statuses)
        
        writer.writerow([
            shipment_id, origin, destination,
            weight_kg, cost_usd, pickup_time, status
        ])

print(f"✅ Generated {NUM_RECORDS} freight records to {OUT_FILE}")
