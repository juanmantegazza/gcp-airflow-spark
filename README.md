# Airflow and Spark project using GCP

## Intro
### What is Cloud Composer?
Cloud Composer is a fully managed workflow orchestration service that empowers you to author, schedule, and monitor pipelines that span across clouds and on-premises data centers. Built on the popular Apache Airflow open source project and operated using the Python programming language, Cloud Composer is free from lock-in and easy to use.

By using Cloud Composer instead of a local instance of Apache Airflow, users can benefit from the best of Airflow with no installation or management overhead.

### What is Apache Airflow?
Apache Airflow is an open source tool used to programmatically author, schedule, and monitor workflows. There are a few key terms to remember relating to Airflow that you'll see throughout the lab:

- DAG - a DAG (Directed Acyclic Graph) is a collection of organized tasks that you want to schedule and run. DAGs, also called workflows, are defined in standard Python files
- Operator - an operator describes a single task in a workflow

### What is Cloud Dataproc?
Cloud Dataproc is Google Cloud Platform's fully-managed Apache Spark and Apache Hadoop service. Cloud Dataproc easily integrates with other GCP services, giving you a powerful and complete platform for data processing, analytics and machine learning.

### What will we do?
Create and run an Apache Airflow workflow in Cloud Composer that completes the following tasks:
- Creates a Cloud Dataproc cluster
- Runs an Apache Spark job on the cluster, and outputs its results to Cloud Storage
- Deletes the cluster