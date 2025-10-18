import os, json
from kafka import KafkaConsumer
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
consumer = KafkaConsumer('events', bootstrap_servers=[BROKER], value_deserializer=lambda m: json.loads(m.decode('utf-8')))
engine = create_engine(DB_URL)

for msg in consumer:
    v = msg.value
    with engine.begin() as conn:
        conn.execute(text("INSERT INTO raw_events (source,event_name,event_payload,event_time) VALUES (:s,:e,:p,:t)"""),
                     {"s": v.get('source','kafka'), "e": v.get('event'), "p": json.dumps(v.get('properties')), "t": v.get('time')})
    print('inserted', v)
