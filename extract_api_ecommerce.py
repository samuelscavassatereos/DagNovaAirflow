from api_hook import ApiHook
import json as js


def test():
    import psycopg2
    try:
        conn = psycopg2.connect("postgresql://postgres:samuel04@192.168.1.80/postgres")
        print("Conexão bem-sucedida com o banco de dados PostgreSQL")
        
        conn.close()
    except Exception as e:
        
        print(f"Erro ao conectar ao banco de dados: {str(e)}")





def extractProducts():
    import psycopg2

    conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="samuel04",
            host="12.168.1.80"
        )
    table_name = 'airflow.products'
    cursor = conn.cursor()
    
    try:
        response = ApiHook.getProducts()
        for var in response:
            json = js.loads(var)
            id = json["id"]   

            select_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
            cursor.execute(select_query, (id,))
            count = cursor.fetchone()[0]

            if count == 0:
                    
                    title = json["title"]     
                    price = json["price"]
                    category = json["category"]
                    description = json["description"]
                    image = json["image"]  
                    
                    insert_query = f"INSERT INTO {table_name} (id, title, price, category,
                    description, image) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (id, title, price, category,
                    description, image))
                    conn.commit()
                    conn.close()
    except:
        OSError.add_note('Erro ao extrair produtos')



        
def extractCarts():
    import psycopg2

    conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="samuel04",
            host="12.168.1.80"
        )
    table_name = 'airflow.carts'
    cursor = conn.cursor()
    
    try:
        response = ApiHook.getCarts()
        for var in response:    
            json = js.loads(var)
            id = json["id"]   

            select_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
            cursor.execute(select_query, (id,))
            count = cursor.fetchone()[0]

            if count == 0:
                    
                    userId = json["userId"]     
                    date = json["date"]
                    products = json["products"]
                    
                    insert_query = f"INSERT INTO {table_name} (id, userId, date, products) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (id, userId, date, products))
                    conn.commit()
                    conn.close()
    except:
        OSError.add_note('Erro ao extrair Carts')



        
def extractUsers():
    import psycopg2

    conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="samuel04",
            host="12.168.1.80"
        )
    table_name = 'airflow.users'
    cursor = conn.cursor()
    
    try:
        response = ApiHook.getUsers()
        for var in response:
            json = js.loads(var)
            id = json["id"]   

            select_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
            cursor.execute(select_query, (id,))
            count = cursor.fetchone()[0]

            if count == 0:
                    
                    email = json["email"]     
                    username = json["username"]
                    password = json["password"]
                    firstname = json["name"]["fisrtname"]
                    lastname = json["name"]["lastname"]
                    city = json["address"]["city"]
                    street = json["address"]["street"]
                    number = json["address"]["number"]
                    zipcode = json["address"]["zipcode"]
                    phone = json["address"]["phone"]   
                    
                    insert_query = f"INSERT INTO {table_name} (id, email, username, password,
                    fisrtname, lastname, city, street, number, zipcode, phone) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
                    cursor.execute(insert_query, (id, email, username, password, firstname, lastname, city, street, number, zipcode, phone))
                    conn.commit()
                    conn.close()
    except:
        print('Erro')
        