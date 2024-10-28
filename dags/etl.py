from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
import os

# Define file paths
SOURCE_FILE = '/opt/airflow/source/input_data.csv'  # Replace with your source file
TRANSFORMED_FILE = '/opt/airflow/dest/transformed_data.csv'  # Destination for transformed data

def extract():
    # Read data from CSV file
    if not os.path.exists(SOURCE_FILE):
        raise FileNotFoundError(f"Source file does not exist: {SOURCE_FILE}")
    
    df = pd.read_csv(SOURCE_FILE)
    return df

def transform(df):
    # Perform simple transformation (e.g., filter out rows where a specific column is NaN)
    transformed_df = df.dropna(subset=['important_column'])  # Replace with your column name
    return transformed_df

def load(df):
    # Write transformed data to a new CSV file
    df.to_csv(TRANSFORMED_FILE, index=False)
    print(f'Transformed data saved to: {TRANSFORMED_FILE}')

with DAG(
    dag_id='simple_etl_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 10, 22),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
        op_kwargs={'df': extract_task.output},  # Pass the output of the extract task
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load,
        op_kwargs={'df': transform_task.output},  # Pass the output of the transform task
    )

    extract_task >> transform_task >> load_task
