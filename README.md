# Google Cloud IAM & BigQuery Service Account Lab

A hands-on Google Cloud project demonstrating service accounts, IAM permissions, Compute Engine, custom IAM roles, and BigQuery access using the Google Cloud Python client library.

## What I implemented

- Created a `devops` service account using the `gcloud` CLI.
- Granted `roles/iam.serviceAccountUser` and `roles/compute.instanceAdmin.v1` to the service account.
- Created a Compute Engine VM named `vm-2` with the service account attached.
- Verified access from the VM with `gcloud compute instances list`.
- Created a project-level custom IAM role from a YAML definition.
- Created a `bigquery-qwiklab` service account.
- Granted BigQuery Data Viewer and BigQuery User roles.
- Created a `bigquery-instance` VM with the BigQuery service account attached.
- Used Python and the Google Cloud BigQuery client library to query a public dataset.

## Technologies

- Google Cloud Platform
- IAM
- Service Accounts
- Compute Engine
- BigQuery
- Python
- Google Cloud Python Client Library
- gcloud CLI

## Repository files

| File | Purpose |
|---|---|
| `query.py` | Authenticates through the Compute Engine service account and queries BigQuery. |
| `role-definition.yaml` | Defines the custom IAM role with Cloud SQL permissions. |
| `.gitignore` | Prevents credentials, keys, environment files, and Python virtual environments from being committed. |

## BigQuery query

The Python program queries the public dataset:

`bigquery-public-data.usa_names.usa_1910_2013`

It filters records for Texas (`TX`), groups by name, orders by total population count, and returns the top 20 names.

## Authentication approach

The project uses the VM's attached Compute Engine service account through `google.auth.compute_engine.Credentials`. No service-account JSON key is required or stored in this repository.

## Example execution

```bash
export PROJECT_ID=$(gcloud config get-value project)
python3 -m venv ~/bq-venv
source ~/bq-venv/bin/activate
python -m pip install google-cloud-bigquery pyarrow pandas db-dtypes
python query.py
```

## Security note

This repository intentionally contains no passwords, private SSH keys, service-account JSON keys, or other secrets. The Google Cloud lab resources are temporary and should not be treated as production infrastructure.

## Skills demonstrated

`Google Cloud` `IAM` `Service Accounts` `Compute Engine` `BigQuery` `Python` `gcloud CLI` `Custom IAM Roles` `Cloud Infrastructure`
