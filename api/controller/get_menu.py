import json
import psycopg2
from flask import jsonify
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP


class GetMenu(MethodView):
    """get all menu """

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
            cur.execute("SELECT * FROM menu")
            m = cur.fetchall()
            columns = ('item_id','item_name','price', 'quantity','amount')
            result = []
            for row in m:
                result.append(dict(zip(columns, row)))
            return jsonify({'Available Menu':result})
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        
