#__init__ file takes teh name of its parent folder, in this case; flaskblog
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#secret key is important for security, need to research further, but it encrypts cookiesd andotehr data.
app.config['SECRET_KEY'] = '015182c115182aa5cc7d6303919cb86d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #instance of database


from flaskblog import routes #done after creating app object to avoid circular importing