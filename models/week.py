from flask.ext.sqlalchemy import SQLAlchemy
#from ffrankings_app import app
import datetime

from models.shared import db

week1start = datetime.date(2015, 9, 8)
week1end = datetime.date(2015, 9, 14)
def get_fantasy_week(today=datetime.date.today()):
    weekend = week1end
    week = 1
    while weekend < today:
        weekend = weekend + datetime.timedelta(days=7)
        week += 1
    return week


class Week(db.Model):
    __tablename__ = "weeks"
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer)
    seeded = db.Column(db.Boolean)

    def is_current_week(self):
        return get_fantasy_week() == self.num

    def __init__(self, num):
        self.num = num
        self.seeded = False

    def __repr__(self):
        return "Week" + str(self.num)
