import json
import psycopg2
from flask import jsonify, request
from db_connection.config import config
import jwt


from flask.views import MethodView
from connect import APP


class UpdateOrderStatus(MethodView):
    """Update order status based on order id"""

    def put(self,id):
        order_status = request.json['order_status']
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            if order_status == "Processing":
                cur.execute("UPDATE orders SET order_status = %s WHERE order_id = %s", (order_status,id,))
                # commit the changes to the database
                conn.commit()
                return jsonify({'message':'Successfully updated the order status to Processing'}), 200
                # commit the changes to the database
                conn.commit()
            elif order_status == "Cancelled":
                cur.execute("UPDATE orders SET order_status = %s WHERE order_id = %s",(order_status,id,))
                # commit the changes to the database
                conn.commit()
                return jsonify({'message':'Successfully updated the order status to Cancelled'}), 200
               
            elif order_status == "Completed":
                cur.execute("UPDATE orders SET order_status = %s  WHERE order_id = %s", (order_status,id,))
                # commit the changes to the database
                conn.commit()
                return jsonify({'message':'Successfully updated the order status to Completed'}), 200

            else:
                return jsonify({"message": "Please provide correct order status"}), 405
            
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return jsonify({'message':'server error'}), 505
        
