from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

# Inicializar db, que conecta con la base de datos
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registrar el blueprint montado en /html
    from .html import html as html_blueprint
    app.register_blueprint(html_blueprint, url_prefix='/html')

    return app
