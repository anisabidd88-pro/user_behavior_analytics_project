import os, pandas as pd
from sqlalchemy import create_engine, text
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

DB_URL = os.getenv('DB_URL', 'postgresql://dbuser:dbpass@localhost:5432/analytics')
engine = create_engine(DB_URL)

def load_aggregates():
    sql = '''select
               coalesce((event_payload::jsonb)->>'user_id','unknown') as user_id,
               min(event_time) as first_seen,
               max(event_time) as last_seen,
               count(*) as total_events
             from raw_events
             group by 1'''
    return pd.read_sql(sql, engine)

def prepare_and_train():
    df = load_aggregates()
    if df.empty:
        print('No data found in raw_events. Run ingestion first.')
        return
    df['recency_days'] = (pd.to_datetime('now') - pd.to_datetime(df['last_seen'])).dt.days
    df['tenure_days'] = (pd.to_datetime(df['last_seen']) - pd.to_datetime(df['first_seen'])).dt.days + 1
    df['churned'] = (df['recency_days'] > 30).astype(int) 
    feat_cols = ['total_events','recency_days','tenure_days']
    X = df[feat_cols].fillna(0)
    y = df['churned']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

if __name__ == '__main__':
    prepare_and_train()
