from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from DagNovaAirflow.extract_api_ecommerce import test, extractCarts, extractProducts, extractUsers

with DAG(
    'extract_api_test',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:

    Sync = BashOperator(
        task_id= 'git_pull',
        bash_command="git pull"
    )

    Test = PythonOperator(
        task_id= 'test',
        python_callable=test
    )

    Users = PythonOperator(
        task_id= 'users',
        python_callable=extractUsers
    )

    Carts = PythonOperator(
        task_id= 'carts',
        python_callable=extractCarts
    )

    Products = PythonOperator(
        task_id= 'products',
        python_callable=extractProducts
    )

    Success = EmptyOperator(
        task_id='success'
    )

Sync >> Test >> [Users, Carts, Products] >> Success
