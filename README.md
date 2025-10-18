# 🧠 User Behavior Analytics Pipeline

A complete end-to-end **User Behavior Analytics System** designed to collect, clean, unify, and analyze user events in real time.  
This project integrates multiple data sources (PostHog, Firebase, server logs), processes them via a modern data pipeline (Python, dbt, Kafka, PostgreSQL), and uses **Machine Learning** to predict user churn.

 
## 🚀 Overview

This system provides a **modular data pipeline** to analyze user behavior across web and mobile platforms.  
It automates ingestion, transformation, real-time streaming, machine learning predictions, and health monitoring — all deployable via Docker.

### Key Capabilities

- 📊 Collects user events from **PostHog**, **Firebase**, and **server logs**
- 🧹 Cleans and unifies data using **dbt**
- ⚡ Streams real-time user events with **Kafka**
- 🧠 Trains a **churn prediction model** using ML
- 🔍 Monitors the pipeline to ensure continuous operation

 
## 🧩 Architecture

sql
             ┌────────────┐
            │   Users     │
            └────┬───────┘
                 │
                 ▼
      ┌────────────────────┐
      │ PostHog / Firebase │
      └────────┬───────────┘
               │
               ▼
     ┌─────────────────────┐
     │ Ingestion (Python)  │
     └────────┬────────────┘
              │
              ▼
      ┌──────────────────┐
      │ PostgreSQL (DB)  │
      └────────┬─────────┘
               │
               ▼
         ┌────────────┐
         │ dbt Models │
         └────┬───────┘
              │
              ▼
   ┌────────────────────┐
   │ Kafka (Real-time)  │
   └────────┬───────────┘
            │
            ▼
    ┌─────────────────┐
    │ ML: Churn Model │
    └────────┬────────┘
             │
             ▼
   ┌────────────────────┐
   │ Monitoring & Alert │
   └────────────────────┘
 
 
## 🛠️ Tech Stack

| Layer | Technology | Description |
|:------|:------------|:-------------|
| Data Sources | **PostHog**, **Firebase**, **Server Logs** | Event tracking and mobile data |
| Ingestion | **Python** | Fetch, clean, and store raw data |
| Storage | **PostgreSQL** | Central unified database |
| Transformation | **dbt** | SQL transformations and data modeling |
| Streaming | **Kafka + Zookeeper** | Real-time event ingestion |
| Machine Learning | **Scikit-learn** | Predict user churn |
| Monitoring | **Python + Cron** | Pipeline health checks |
| Infrastructure | **Docker Compose** | Easy local deployment |

 
## 🧠 Project Structure

user_behavior_analytics_project/
│
├── ingestion/ # Data ingestion scripts
│ ├── posthog_ingest.py
│ ├── firebase_ingest.py
│ └── logs_ingest.py
│
├── dbt/ # dbt models for data transformation
│ └── models/
│ ├── staging/
│ └── marts/
│
├── kafka/ # Real-time streaming components
│ ├── producer.py
│ └── consumer.py
│
├── ml/ # Machine Learning models
│ └── train_churn_example.py
│
├── monitoring/ # Pipeline monitoring scripts
│ └── monitor_pipeline.py
│
├── infra/ # Infrastructure setup
│ ├── init_db.py
│ └── docker-compose.yml
│
├── .env.template # Environment variable template
├── connector_config_template.json # Fivetran config (optional)
├── run_local.sh # Script to start the pipeline locally
└── README.md

  
 
## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
 git clone https://github.com/anisabidd88-pro/user_behavior_analytics_project.git
cd user_behavior_analytics_project
2️⃣ Configure environment variables
Copy and edit the environment file:

 
 cp .env.template .env
Then fill in your credentials:

 
 POSTGRES_USER=analytics_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=analytics_db
POSTGRES_HOST=localhost
3️⃣ Start the infrastructure (DB + Kafka)
 
 docker-compose up -d
4️⃣ Initialize the database
 
 python infra/init_db.py
5️⃣ Run ingestion
 
 python ingestion/posthog_ingest.py
python ingestion/firebase_ingest.py
python ingestion/logs_ingest.py
6️⃣ Transform data with dbt
 
 cd dbt
dbt run
7️⃣ Start Kafka streaming
 
 python kafka/producer.py
python kafka/consumer.py
8️⃣ Train and evaluate the churn model
 
 python ml/train_churn_example.py
9️⃣ Start monitoring
 
 python monitoring/monitor_pipeline.py
📈 Output
analytics_db PostgreSQL database with:

raw_events — all ingested user events

stg_events — cleaned staging tables

mart_user_scoring — analytical model outputs

ML model output predicting user churn probabilities.

Real-time event stream via Kafka.

Alerts on pipeline performance issues.

🧩 Example Use Cases
Detect users likely to stop using the app (churn prediction)

Identify top-performing marketing channels

Real-time analytics dashboard for user behavior

Feed data to recommendation engines or personalization systems

🧠 Future Enhancements
Add Airflow for full orchestration

Deploy ML model as an API (FastAPI/Flask)

Integrate with BI tools (Metabase / Superset)

Add anomaly detection in user behavior

🤝 Contributing
Contributions, improvements, and new features are welcome!
Fork the repository, create a branch, and submit a pull request.

📜 License
This project is released under the MIT License.

💬 Author
Developed by:Anis Abid

