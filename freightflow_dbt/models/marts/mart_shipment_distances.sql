-- models/marts/mart_shipment_distances.sql
-- uses euclidean distance formula

with enriched as (
    select *
    from {{ ref('int_enriched_shipments') }}
),

with_distance as (
    select
        *,
        sqrt(
            pow((origin_lat - dest_lat), 2) +
            pow((origin_lon - dest_lon), 2)
        ) as approx_distance
    from enriched
)

select * from with_distance
