"""Airflow DAG that creates a Dataproc Cluster using BashOperator, runs a Dataproc Job
and deletes the cluster using BashOperator.
"""

import airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.utils.dates import days_ago

# project variables
PROJECT_ID = 'insert gcp project'
REGION = 'insert region'
PYSPARK_URI = 'instert pyspark script gcs uri'

# cluster
CLUSTER_NAME = 'instert cluster name'

# pyspark job
PYSPARK_JOB = {
    "reference": {"project_id": PROJECT_ID},
    "placement": {"cluster_name": CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": PYSPARK_URI},
}

# default args
default_args = {
    'project_id': PROJECT_ID,
    'start_date': days_ago(1),
    'retries': 0
}

# Define a DAG of tasks.
with DAG(
    dag_id='dataproc_job',
    default_args=default_args,
    schedule_interval=None,
) as dag:

    t1 = BashOperator(
        task_id='create_cluster',
        bash_command='gcloud dataproc clusters create {CLUSTER_NAME} \
            --region {REGION} \
            --initialization-actions gs://goog-dataproc-initialization-actions-us-central1/connectors/connectors.sh \
            --metadata spark-bigquery-connector-version=0.23.2'
    )
    
    t2 = DataprocSubmitJobOperator(
        task_id='pyspark_task',
        job=PYSPARK_JOB,
        project_id=PROJECT_ID,
        location=REGION
    )

    t3 = BashOperator(
        task_id='delete_cluster',
        bash_command='gcloud dataproc clusters delete {CLUSTER_NAME} \
            --region us-central1'
    )
    
    t1 >> t2 >> t3