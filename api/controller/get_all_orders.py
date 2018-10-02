import json
import psycopg2
from flask import jsonify
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP


class GetAllOrders(MethodView):
    """get all orders"""

    def get(self):
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute("SELECT order_id,order_item_name,order_item_rate,order_item_quantity,order_item_amount,location,order_status FROM orders")
            all_orders = cur.fetchall()
            columns = ('order_id','order_item_name','order_item_rate','order_item_quantity','order_item_amount','location','order_status')
            result = []
            for row in all_orders:
                result.append(dict(zip(columns, row)))
            return jsonify({'Available User Orders': result})
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return jsonify({'message':'No id required'}), 404
        
