import os, csv, json, time
from datetime import datetime
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
SAMPLE = os.getenv('POSTHOG_SAMPLE', '../sample_data/posthog_sample.csv')

engine = create_engine(DB_URL, pool_pre_ping=True)

def load_csv_to_db(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with engine.begin() as conn:
        for r in rows:
            payload = r.get('event_properties') or '{}'
            try:
                conn.execute(text("""INSERT INTO raw_events (source,event_name,event_payload,event_time)
                                  VALUES (:source,:event,:payload,:etime)"""),
                             {"source":"posthog","event":r['event_name'],"payload":payload,"etime":r['event_time']})
            except Exception as e:
                print('insert error', e, r)
    print(f'loaded {len(rows)} rows from {path}')

if __name__ == '__main__':
    load_csv_to_db(SAMPLE)
