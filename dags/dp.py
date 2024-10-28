from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import shutil
import os
import logging

SOURCE_DIR = '/opt/airflow/source'  # Use the Linux path for the container
DEST_DIR = '/opt/airflow/dest'       # Use the Linux path for the container

def move_files():
    if not os.path.exists(SOURCE_DIR):
        logging.error(f"Source directory does not exist: {SOURCE_DIR}")
        raise FileNotFoundError(f"Source directory does not exist: {SOURCE_DIR}")

    logging.info(f"Current working directory: {os.getcwd()}")
    logging.info(f"Contents of /opt/airflow: {os.listdir('/opt/airflow')}")

    # Move files
    for filename in os.listdir(SOURCE_DIR):
        source_file = os.path.join(SOURCE_DIR, filename)
        destination_file = os.path.join(DEST_DIR, filename)

        # Move the file only if it's a file
        if os.path.isfile(source_file):
            shutil.move(source_file, destination_file)
            logging.info(f'Moved: {source_file} to {destination_file}')

with DAG(
    dag_id='file_move_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 10, 22),
    catchup=False,
) as dag:

    move_files_task = PythonOperator(
        task_id='move_files_task',
        python_callable=move_files,
    )

    move_files_task
