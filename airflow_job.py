from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
import pandas as pd
import shutil
import logging

# Chemins relatifs
to_process_dir = '/mnt/d/Booster Data IA/toProcess'
processed_dir = '/mnt/d/Booster Data IA/already_processed'
result_dir = '/mnt/d/Booster Data IA/result'

# Assurez-vous que les répertoires existent
os.makedirs(to_process_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)
os.makedirs(result_dir, exist_ok=True)

def process_csv_files():
    logging.info(f"Processing directory: {to_process_dir}")
    for filename in os.listdir(to_process_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(to_process_dir, filename)
            logging.info(f"Processing file: {file_path}")
            try:
                df = pd.read_csv(file_path)
                avg_price = df['price'].mean()
                result_filename = f'result_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
                result_path = os.path.join(result_dir, result_filename)
                df_result = pd.DataFrame({'avg_price': [avg_price]})
                df_result.to_csv(result_path, index=False)
                shutil.move(file_path, os.path.join(processed_dir, filename))
                logging.info(f"File {filename} processed and moved to {processed_dir}")
            except Exception as e:
                logging.error(f"Error processing file {filename}: {e}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'process_csv',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=1),
)

t1 = PythonOperator(
    task_id='process_csv_files',
    python_callable=process_csv_files,
    dag=dag,
)

t1
