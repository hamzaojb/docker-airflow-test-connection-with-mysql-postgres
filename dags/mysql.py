from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 4),
}

with DAG('create_table_in_mysql', default_args=default_args, schedule_interval='@once') as dag:
    
    create_table_task = MySqlOperator(
        task_id='create_table_task',
        mysql_conn_id='mysql_conn_id',  # Your MySQL connection ID
        sql="""
        CREATE TABLE IF NOT EXISTS clients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
    )

    create_table_task
