-- models/staging/stg_freight_tracking.sql
select
  cast(shipment_id as string) as shipment_id,
  lower(replace(last_known_location, ' ', '_')) as last_known_location,
  last_update_time,  -- No need to cast or parse
  status_update
from read_csv_auto('../freight_data/freight_tracking.csv')
