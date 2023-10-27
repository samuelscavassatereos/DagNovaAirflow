from api_hook import ApiHook

db_url = "postgresql://postgres:samuel04@192.168.1.80/postgres"

def test():
    import psycopg2
    try:
        conn = psycopg2.connect(db_url)
        print("Conexão bem-sucedida com o banco de dados PostgreSQL")
        
        conn.close()
    except Exception as e:
        
        print(f"Erro ao conectar ao banco de dados: {str(e)}")

def extractProducts():
    import pandas as pd
    from sqlalchemy import create_engine
    try:
        response = ApiHook.getProducts()
        for json in response:
            df = pd.DataFrame([json])           
            engine = create_engine(db_url)
            df.to_sql('products', con=engine, if_exists='append', index=False, method='multi', chunksize=1000, 
          schema='airflow')
    except:
        OSError.add_note('Erro ao extrair produtos')
        
def extractCarts():
    import pandas as pd
    from sqlalchemy import create_engine
    try:
        response = ApiHook.getCarts()
        for json in response:
            df = pd.DataFrame([json])           
            engine = create_engine(db_url)
            df.to_sql('airflow.carts', con=engine, if_exists='append', index=False, method='multi', chunksize=1000, 
          schema='airflow')
    except:
        OSError.add_note('Erro ao extrair Carts')
        
def extractUsers():
    import pandas as pd
    from sqlalchemy import create_engine
    try:
        response = ApiHook.getUsers()
        for json in response:
            df = pd.DataFrame([json])           
            engine = create_engine(db_url)
            df.to_sql('airflow.users', con=engine, if_exists='append', index=False, method='multi', chunksize=1000, 
          schema='airflow')
    except:
        print('Erro')
        