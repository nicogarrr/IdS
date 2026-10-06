from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config

# Crear el objeto db que servirá para conectar con la base de datos
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    from app import models

    @app.route('/amigos')
    def hola_mundo():
        from app.models import Amigo
        amigos = Amigo.query.all()
        return render_template('tabla_amigos.html', amigos=amigos)

    return app
