# FreightFlow DBT Project 🚚📦

This project simulates a modern freight tracking pipeline using:

- **dbt + DuckDB** for data transformation and enrichment  
- **Google Pub/Sub** for streaming shipment status updates  
- **Python** scripts to generate, enrich, and simulate real-time freight activity

---

## 💡 Project Features

- **Data Modeling with dbt**  
  - Staging, intermediate, and mart layers  
  - Joins shipment data with coordinate enrichment  
  - Calculates approximate distances between origin and destination  

- **Streaming with Google Pub/Sub**  
  - `publisher.py` sends real-time tracking updates  
  - `subscriber.py` listens and processes those updates  

- **Fake Data Generation**  
  - Shipment and tracking data generated using Python and `Faker`  
  - Location coordinates added via `geopy`

---

## 🛠️ How to Use

### Setup
```bash

# Install dependencies
pip install -r requirements.txt

# Run dbt models
dbt seed         # Load seed data (like city coordinates)
dbt run          # Run transformations and create views

# simulate messages
python3 pubsub_sim/subscriber.py
python3 pubsub_sim/publisher.py