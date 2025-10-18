#!/usr/bin/env bash
set -euo pipefail
echo "1) start docker infra (postgres + kafka)"
docker-compose up -d
echo "2) initialize DB schema"
python infra/init_db.py
echo "3) ingest sample data"
python ingestion/ingest_all.py
echo "4) run a quick ml training (toy)"
python ml/train_churn_example.py
echo "Demo complete."
