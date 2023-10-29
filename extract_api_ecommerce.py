from DagNovaAirflow.api_hook import ApiHook
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
    conn = psycopg2.connect("postgresql://postgres:samuel04@192.168.1.80/postgres")
    table_name = 'airflow.products'
    cursor = conn.cursor()

    #try:
    response = ApiHook.getProducts()
    for json in response:

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
                insert_query = f"INSERT INTO {table_name} (id, title, price, category, descreption, image) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (id, title, price, category, description[:200], image))
                conn.commit()
    conn.close()


    #except:
        #print('Erro ao extrair produtos')



def extractCarts():
    import psycopg2

    conn = psycopg2.connect("postgresql://postgres:samuel04@192.168.1.80/postgres")
    table_name = 'airflow.carts'
    cursor = conn.cursor()


    response = ApiHook.getCarts()
    for json in response:

        id = json["id"]

        select_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
        cursor.execute(select_query, (id,))
        count = cursor.fetchone()[0]

        if count == 0:

                    userId = json["userId"]
                    date = json["date"]
                    products = json["products"]

                    insert_query = f"INSERT INTO {table_name} (id, userId, date, products) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_query, (id, userId, date, str(products)))
                    conn.commit()
    conn.close()





def extractUsers():
    import psycopg2

    conn = psycopg2.connect("postgresql://postgres:samuel04@192.168.1.80/postgres")
    table_name = 'airflow.users'
    cursor = conn.cursor()

    response = ApiHook.getUsers()
    for json in response:
        id = json["id"]
        select_query = f"SELECT COUNT(*) FROM {table_name} WHERE id = %s"
        cursor.execute(select_query, (id,))
        count = cursor.fetchone()[0]
        if count == 0:

                    email = json["email"]
                    username = json["username"]
                    password = json["password"]
                    firstname = json["name"]["fisrt_name"]
                    lastname = json["name"]["last_name"]
                    city = json["address"]["city"]
                    street = json["address"]["street"]
                    number = json["address"]["number"]
                    zipcode = json["address"]["zipcode"]
                    phone = json["address"]["phone"]
                    lat=None
                    long=None

                    insert_query = f"INSERT INTO {table_name} (id, email, username, password, first_name, last_name, city, street, number, zipcode, lat, long, phone) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (int(id), email, username, password, firstname, lastname, city, street, number, zipcode, lat, long, phone))
                    conn.commit()
    conn.close()

