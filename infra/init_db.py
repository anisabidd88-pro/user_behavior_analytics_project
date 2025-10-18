import os
from sqlalchemy import create_engine, text

DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
engine = create_engine(DB_URL)

with engine.begin() as conn:
    conn.execute(text('''
        create table if not exists raw_events (
          id serial primary key,
          source varchar not null,
          event_name varchar not null,
          event_payload jsonb,
          event_time timestamptz not null
        );
    '''))
    conn.execute(text('''
        create table if not exists users (
          user_id varchar primary key,
          first_seen timestamptz,
          last_seen timestamptz,
          email varchar,
          properties jsonb
        );
    '''))
print("Initialized DB schema.")
