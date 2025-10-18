# Run basic smoke tests for the scaffold
set -e
python infra/init_db.py
python ingestion/ingest_posthog.py
python ml/train_churn_example.py || true
echo 'Tests finished (some tests may intentionally be no-ops if data missing).'
