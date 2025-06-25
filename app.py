from flask import Flask
from utils.database import db
from flask_migrate import Migrate
import os
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev')

db.init_app(app)
migrate = Migrate(app, db)

print("Ruta absoluta de la base de datos:", os.path.abspath('db.sqlite3'))

# Ahora importa y registra blueprints
from controllers.venta_controller import main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(debug=True)