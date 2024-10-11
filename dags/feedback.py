from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 4),
}

with DAG('insert_employee_feedback_summary', default_args=default_args, schedule_interval='@once') as dag:
    
    # Tâche pour créer la table
    create_table_task = PostgresOperator(
        task_id='create_table_task',
        postgres_conn_id='postgres_conn_id',  # Remplacez par votre ID de connexion PostgreSQL
        sql="""
        CREATE TABLE IF NOT EXISTS employee_feedback_summary (
            employee_name VARCHAR(100),
            department_name VARCHAR(100),
            feedback_rating INT,
            employee_gender VARCHAR(100)
        );
        """
    )

    # Tâche pour insérer les données
    insert_data_task = PostgresOperator(
        task_id='insert_employee_feedback_data',
        postgres_conn_id='postgres_conn_id',  # Remplacez par votre ID de connexion PostgreSQL
        sql="""
        INSERT INTO employee_feedback_summary (employee_name, department_name, feedback_rating,employee_gender )
        SELECT 
            e.name AS employee_name, 
            d.name AS department_name, 
            f.rating AS feedback_rating,
            e.gender AS employee_gender

        FROM 
            employees e
        JOIN 
            departments d ON e.department_id = d.id
        LEFT JOIN 
            feedback f ON e.id = f.employee_id;
        """
    )

    # Définir l'ordre des tâches
    create_table_task >> insert_data_task
