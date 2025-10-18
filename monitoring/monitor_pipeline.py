import os, smtplib, logging
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
engine = create_engine(DB_URL)

def check_freshness(threshold_minutes=60):
    with engine.connect() as conn:
        res = conn.execute(text('select max(event_time) as last_event from raw_events')).fetchone()
        last = res['last_event']
        if last is None:
            logging.error('No events ingested yet.')
            return False
        age = datetime.utcnow() - last.replace(tzinfo=None)
        if age > timedelta(minutes=threshold_minutes):
            logging.error(f'Latest event is stale: {age} old')
            return False
        logging.info('Pipeline is fresh.')
        return True

if __name__ == '__main__':
    ok = check_freshness()
    print('Pipeline OK?', ok)
