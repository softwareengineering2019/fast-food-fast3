import psycopg2
from config import config
 
 
def create_tables():
    """ create tables in the fast_food_fast database"""
    queries = (
                """ CREATE TABLE IF NOT EXISTS accounts (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        phone VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        roles VARCHAR(255) NOT NULL DEFAULT ('User')
                        )
                """,
                """
                    CREATE TABLE IF NOT EXISTS menu (
                        item_id SERIAL  PRIMARY KEY,
                        item_name VARCHAR(255) NOT NULL,
                        price INT NOT NULL,
                        quantity INT NOT NULL,
                        amount INT NOT NULL
                    )
                """,
                """ 
                    CREATE TABLE IF NOT EXISTS  orders (
                        order_id SERIAL PRIMARY KEY,
                        user_id INTEGER REFERENCES accounts(id) ON DELETE CASCADE,
                        menu_id INTEGER REFERENCES menu(item_id) ON DELETE CASCADE,
                        order_item_name VARCHAR(255) NOT NULL,
                        order_item_rate VARCHAR(255) NOT NULL,
                        order_item_quantity VARCHAR(255) NOT NULL,
                        order_item_amount VARCHAR(255) NOT NULL,
                        location VARCHAR(255) NOT NULL,
                        order_status VARCHAR(255) DEFAULT ('New')
                    )
                """
            )

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for query in queries:
            cur.execute(query)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
 
if __name__ == '__main__':
    create_tables()