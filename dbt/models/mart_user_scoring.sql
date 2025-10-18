with events as (
  select
    coalesce(props->>'user_id', props->>'distinct_id', 'unknown') as user_id,
    event_name,
    event_time
  from {{ ref('staging_raw_events') }}
),
agg as (
  select user_id,
         min(event_time) as first_seen,
         max(event_time) as last_seen,
         count(*) filter (where event_name = 'signup') as signups,
         count(*) as total_events
  from events
  group by user_id
)
select user_id,
       first_seen,
       last_seen,
       total_events,
       signups,
       -- basic scoring heuristic:
       (least(100, total_events) + signups*20) as user_score
from agg
