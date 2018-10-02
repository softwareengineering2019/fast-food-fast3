import flask


APP = flask.Flask(__name__)

secret_key = APP.config['SECRET_KEY'] = 'secretkey'