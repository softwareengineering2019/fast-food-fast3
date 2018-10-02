import json
import psycopg2
from flask import jsonify
from flask import request
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP
from flask import Response

class PostMenu(MethodView):
    """ add meal option"""
    def post(self):

        """ insert a new meal to the menu """

        sql11 = """INSERT INTO menu (item_name,price,quantity,amount)
                VALUES(%s,%s,%s,%s);"""
        
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql11, (request.json['item_name'],request.json['price'],request.json['quantity'],request.json['amount']),)
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            return jsonify({'message':'Admin has successfully added meal option to the menu'})
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return jsonify({'Message': 'Invalid response'})
