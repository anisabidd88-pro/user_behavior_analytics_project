import csv, os, json, time
from kafka import KafkaProducer

SAMPLE = os.getenv('POSTHOG_SAMPLE', '../sample_data/posthog_sample.csv')
BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')

def main():
    producer = KafkaProducer(bootstrap_servers=[BROKER], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    with open(SAMPLE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            msg = {'source': r['source'], 'event': r['event_name'], 'properties': r.get('event_properties'), 'time': r['event_time']}
            producer.send('events', msg)
            print('sent', msg)
            time.sleep(0.2)
    producer.flush()

if __name__ == '__main__':
    main()
