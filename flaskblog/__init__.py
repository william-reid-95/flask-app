#__init__ file takes teh name of its parent folder, in this case; flaskblog
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#secret key is important for security, need to research further, but it encrypts cookiesd andotehr data.
app.config['SECRET_KEY'] = '015182c115182aa5cc7d6303919cb86d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #instance of database
bcrypt = Bcrypt(app) #instance of encrypter
login_manager = LoginManager(app) #instance of login manager
login_manager.login_view = 'login' #the function name (route) of the page to navigate to, if a user is not logged in and lands on a page that requires login.
login_manager.login_message_category = 'info' # set the category (css) of the info flash message

#routes must be imported into init otherwise pages cannot be accesed
#done after creating app object to avoid circular importing
from flaskblog import routes 