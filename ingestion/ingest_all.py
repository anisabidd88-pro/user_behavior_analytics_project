import os, subprocess
scripts = ['ingest_posthog.py','ingest_logs.py']
here = os.path.dirname(__file__)
for s in scripts:
    print('Running', s)
    subprocess.run(['python', os.path.join(here, s)], check=True)
print('All ingestion steps completed.')
