from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class StoreStatus(db.Model):
    __tablename__ = "store_status"

    store_id = db.Column(db.BigInteger, primary_key=True)
    status = db.Column(db.Text)
    timestamp_utc = db.Column(db.Text)

    def __init__(self, store_id, status, timestamp_utc):
        self.store_id = store_id
        self.status = status
        self.timestamp_utc = timestamp_utc


class TimeZone(db.Model):
    __tablename__ = "time_zone"

    store_id = db.Column(db.BigInteger, primary_key=True)
    timezone_str = db.Column(db.Text)

    def __init__(self, store_id, timezone_str):
        self.store_id = store_id
        self.timezone_str = timezone_str


class BusinessHours(db.Model):
    __tablename__ = "business_hours"

    store_id = db.Column(db.BigInteger, primary_key=True)
    day_of_week = db.Column(db.String)
    opening_time = db.Column(db.String)
    closing_time = db.Column(db.String)

    def __init__(self, store_id, day_of_week, opening_time, closing_time):
        self.store_id = store_id
        self.day_of_week = day_of_week
        self.opening_time = opening_time
        self.closing_time = closing_time
