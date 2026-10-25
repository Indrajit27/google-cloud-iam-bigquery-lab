from google.auth import compute_engine
from google.cloud import bigquery

# The project ID is set through the PROJECT_ID environment variable.
# Example: export PROJECT_ID=$(gcloud config get-value project)
import os

project_id = os.environ["PROJECT_ID"]

credentials = compute_engine.Credentials(
    service_account_email=f"bigquery-qwiklab@{project_id}.iam.gserviceaccount.com"
)

query = """
SELECT name, SUM(number) AS total_people
FROM `bigquery-public-data.usa_names.usa_1910_2013`
WHERE state = 'TX'
GROUP BY name
ORDER BY total_people DESC
LIMIT 20
"""

client = bigquery.Client(
    project=project_id,
    credentials=credentials,
)

results = client.query(query).to_dataframe()
print(results)
