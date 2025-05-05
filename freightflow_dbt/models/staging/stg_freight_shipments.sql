-- models/staging/stg_freight_shipments.sql
select
  cast(shipment_id as string) as shipment_id,
  lower(replace(origin, ' ', '_')) as origin,
  lower(replace(destination, ' ', '_')) as destination,
  cast(weight_kg as integer) as weight_kg,
  cast(cost_usd as float) as cost_usd,
  cast(pickup_time as timestamp) as pickup_timestamp,
  status
from read_csv_auto('../freight_data/freight_shipments.csv')
