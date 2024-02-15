from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_socketio import SocketIO
from flask_admin import Admin
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
socketio=SocketIO()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['DEBUG'] = True
    # admin = Admin(app, name='microblog', template_mode='bootstrap3')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)


    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.chat.routes import chat
    # from flaskblog.admin.routes import admin
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(chat)
    # app.register_blueprint(admin)
    
    return app