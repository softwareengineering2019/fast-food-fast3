import jwt
import psycopg2
from flask import request
from flask import jsonify
from functools import wraps 
from database.config import config
from connect import secret_key

def token_required(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message':'Token is missing!'}),401
        try:
            data = jwt.decode(token, secret_key)
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute("SELECT * FROM accounts WHERE email=%s",(data['email'], ))
            current_user = cur.fetchall()
        except:
            return jsonify({'message':'Invalid Token!'}),401
        return f(self, current_user, *args, **kwargs)
    return decorated