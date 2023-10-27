from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
import extract_api_ecommerce 

with DAG(
    'Extract API test',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:
    
    Test = PythonOperator(
        task_id= 'Test',
        callable = extract_api_ecommerce.test
    )
    
    Users = PythonOperator(
        task_id= 'Users',
        callable = extract_api_ecommerce.extractUsers
    )

    Carts = PythonOperator(
        task_id= 'Carts',
        callable = extract_api_ecommerce.extractCarts
    )

    Products = PythonOperator(
        task_id= 'Products',
        callable = extract_api_ecommerce.extractProducts
    )

    Success = EmptyOperator(
        task_id='Success'
    )

Test >> [Users, Carts, Products] >> Success
