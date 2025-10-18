with raw as (
  select * from {{ ref('raw_events') }} 
),
parsed as (
  select
    id,
    source,
    event_name,
    cast(event_time as timestamptz) as event_time,
    case when jsonb_typeof(event_payload::jsonb) is not null then event_payload::jsonb end as props
  from raw
)
select distinct on (id) id, source, event_name, event_time, props
from parsed
order by id, event_time desc
