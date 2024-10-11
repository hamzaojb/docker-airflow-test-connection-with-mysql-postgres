from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 4),
}

with DAG('create_table_in_postgres', default_args=default_args, schedule_interval='@once') as dag:
    
    create_table_task = PostgresOperator(
        task_id='create_table_task',
        postgres_conn_id='postgres_conn_id',  # Assurez-vous que c'est bien le bon ID de connexion
        sql="""
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
    )

    create_table_task
