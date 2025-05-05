with shipments as (
    select *
    from {{ ref('stg_freight_shipments') }}
),

origin_coords as (
    select
        city || ', ' || state as location,
        latitude as origin_lat,
        longitude as origin_lon
    from {{ ref('city_coords') }}
),

dest_coords as (
    select
        city || ', ' || state as location,
        latitude as dest_lat,
        longitude as dest_lon
    from {{ ref('city_coords') }}
)

select
    s.*,
    o.origin_lat,
    o.origin_lon,
    d.dest_lat,
    d.dest_lon
from shipments s
left join origin_coords o 
  on lower(replace(o.location, ' ', '_')) = s.origin
left join dest_coords d 
  on lower(replace(d.location, ' ', '_')) = s.destination
