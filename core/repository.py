from core.db import db
from core.db import TimeZone, BusinessHours, StoreStatus
from flask import Flask
from importlib import import_module
import wrapper
from sqlalchemy import text

class ReportRepository:
    @staticmethod
    def find_store_status_by_store_id(store_id):
        with wrapper.app.app.app_context():
            query = text("SELECT * FROM store_monitoring.store_status WHERE store_id = :store_id")
            result = db.session.execute(query, {'store_id': store_id})
            all_status = result.fetchall() 
            
            for row in all_status:
                print(row) 