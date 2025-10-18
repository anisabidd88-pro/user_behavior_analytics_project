import csv, os, json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
SAMPLE = os.getenv('LOGS_SAMPLE', '../sample_data/logs_sample.csv')
engine = create_engine(DB_URL, pool_pre_ping=True)

def run():
    import time
    with open(SAMPLE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with engine.begin() as conn:
            for r in reader:
                conn.execute(
                    text("INSERT INTO raw_events(source,event_name,event_payload,event_time) VALUES (:s,:e,:p,:t)"),
                    {"s": "server", "e": r.get('event', 'http_request'),
                     "p": json.dumps({"path": r.get('path'), "status": r.get('status')}),
                     "t": r.get('time')}
                )
    print('logs ingested')

if __name__ == '__main__':
    run()
