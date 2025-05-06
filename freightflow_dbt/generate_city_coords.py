import pandas as pd
from geopy.geocoders import Nominatim
import time
import os

# File paths
shipment_path = "freight_data/freight_shipments.csv"
tracking_path = "freight_data/freight_tracking.csv"
output_path = "freightflow_dbt/data/city_coords.csv"

# Load cities from both CSVs
df_shipments = pd.read_csv(shipment_path)
df_tracking = pd.read_csv(tracking_path)

# Combine city/state values from origin, destination, and last_known_location
cities = pd.concat([
    df_shipments["origin"],
    df_shipments["destination"],
    df_tracking["last_known_location"]
]).dropna().unique()

# Deduplicate and standardize
cleaned = list(set(cities))
cleaned.sort()

# Initialize geopy
geolocator = Nominatim(user_agent="freight_location_enricher")

# Geocode results
results = []
for place in cleaned:
    try:
        location = geolocator.geocode(place)
        if location:
            city, state = place.split(", ")
            results.append({
                "city": city.strip(),
                "state": state.strip(),
                "latitude": location.latitude,
                "longitude": location.longitude
            })
            print(f"✔ {place}: {location.latitude}, {location.longitude}")
        else:
            print(f"❌ Not found: {place}")
    except Exception as e:
        print(f"⚠️ Error with {place}: {e}")
    time.sleep(1)  

# Save to CSV
os.makedirs(os.path.dirname(output_path), exist_ok=True)
pd.DataFrame(results).to_csv(output_path, index=False)
print(f"\n✅ Saved {len(results)} locations to {output_path}")
