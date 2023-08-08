# wrapper/app.py
from flask import Flask
from core.db import db
from wrapper.controller import controller_bp
from sqlalchemy import text

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:19630821@localhost:3306/store_monitoring"

db.init_app(app)
app.register_blueprint(controller_bp)

with app.app_context():
    try:
        result = db.session.execute(text("SELECT 1")).scalar()
        if result == 1:
            print("Successfully connected to the Database")
    except Exception as e:
        print("Failed to connect to the Database:", e)
