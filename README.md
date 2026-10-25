# Google Cloud IAM & BigQuery Service Account Lab

A hands-on Google Cloud project demonstrating service accounts, IAM permissions, Compute Engine, custom IAM roles, and BigQuery access using the Google Cloud CLI and Python client library.

## Lab

- **Challenge Lab:** Configure Service Accounts and IAM Roles for Google Cloud
- **Lab ID:** ARC134
- **Primary services:** IAM, Service Accounts, Compute Engine, BigQuery

## What I implemented

- Created a `devops` service account using the `gcloud` CLI.
- Granted IAM permissions required for Compute Engine administration and service-account usage.
- Created a Compute Engine VM named `vm-2` and attached a service account.
- Verified Compute Engine resources from Cloud Shell and the VM.
- Created a project-level custom IAM role from a YAML definition.
- Created a `bigquery-qwiklab` service account.
- Granted BigQuery Data Viewer and BigQuery User permissions.
- Created a `bigquery-instance` VM with the BigQuery service account attached.
- Connected to the VM using SSH.
- Created a Python virtual environment and installed the Google Cloud BigQuery client library.
- Used the VM's attached service account for application authentication instead of storing a service-account JSON key.
- Queried a public BigQuery dataset and displayed the results with Python.

## Technologies

- Google Cloud Platform
- Cloud IAM
- Service Accounts
- Compute Engine
- BigQuery
- Python
- Google Cloud Python Client Library
- gcloud CLI
- Custom IAM Roles

## Repository structure

| File | Purpose |
|---|---|
| `query.py` | Python example that authenticates with the VM service account and runs a BigQuery query. |
| `role-definition.yaml` | Example custom IAM role definition used for the lab. |
| `.gitignore` | Prevents credentials, keys, environment files, and Python virtual environments from being committed. |
| `README.md` | Project overview, implementation notes, commands, and skills demonstrated. |

## BigQuery example

The lab uses the public `publicdata.samples.natality` dataset. The example query filters records for years after 2000 and groups the results by year.

```sql
SELECT
  year,
  COUNT(1) AS num_babies
FROM
  publicdata.samples.natality
WHERE
  year > 2000
GROUP BY
  year
ORDER BY
  year;
```

## Authentication approach

The Python example uses the Compute Engine service account through `google.auth.compute_engine.Credentials`. No service-account JSON key is required or stored in this repository.

## Example execution

```bash
export PROJECT_ID=$(gcloud config get-value project)
python3 -m venv ~/myvenv
source ~/myvenv/bin/activate
python -m pip install --upgrade pip
python -m pip install google-cloud-bigquery pyarrow pandas db-dtypes
python query.py
```

## IAM example commands

```bash
gcloud iam service-accounts create bigquery-qwiklab \
  --display-name="bigquery-qwiklab"

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
  --member="serviceAccount:bigquery-qwiklab@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataViewer"

gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID \
  --member="serviceAccount:bigquery-qwiklab@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/bigquery.user"
```

## Security note

This repository intentionally contains no passwords, private SSH keys, service-account JSON keys, or other secrets. Google Cloud Skills Boost lab resources are temporary and should not be treated as production infrastructure.

## Skills demonstrated

`Google Cloud` `IAM` `Service Accounts` `Compute Engine` `BigQuery` `Python` `gcloud CLI` `Custom IAM Roles` `Cloud Infrastructure` `Cloud Security`
