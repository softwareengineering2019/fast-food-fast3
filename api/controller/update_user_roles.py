import json
import psycopg2
from flask import jsonify, request
from db_connection.config import config
import jwt
from flask.views import MethodView
from connect import APP


class UpdateUserRoles(MethodView):
    """Update user role based on id"""

    def put(self,id):
        roles = request.json['roles']
        conn = None
        try:
            # read the connection parameters
            params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            if roles == "Admin":
                cur.execute("UPDATE accounts SET roles = %s WHERE id = %s", (roles,id,))
                # commit the changes to the database
                conn.commit()
                return jsonify({'message':'Successfully updated the user role to an Admin'}), 200
                # commit the changes to the database
                conn.commit()
            else:
                return jsonify({"message": "Wrong access rights, please grant admin rights to this user"}), 405
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return jsonify({'message':'server error'}), 505
        
