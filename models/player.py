from flask.ext.sqlalchemy import SQLAlchemy
#from ffrankings_app import app
import datetime

db = SQLAlchemy()

week1end = datetime.date(2015, 9, 14)
def get_fantasy_week(today=datetime.date.today()):
    weekend = week1end
    week = 1
    while weekend < today:
        weekend = weekend + datetime.timedelta(days=7)
        week += 1
    return week

# Create our database models
class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    position = db.Column(db.String(120))
    team = db.Column(db.String(120))
    elo = db.Column(db.String(127))
    eloPPR = db.Column(db.String(127))
    eloHalf = db.Column(db.String(127))
    flexElo = db.Column(db.String(127))
    flexEloPPR = db.Column(db.String(127))
    flexEloHalf = db.Column(db.String(127))
    url = db.Column(db.String(120))

    def get_week_elo(self):

        week = get_fantasy_week()
        elo_week = float((self.elo.split(","))[week-1])

        return elo_week


    def __init__(self, name, position, team, url):
        self.name = name
        self.position = position
        self.team = team
        self.elo = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.eloPPR = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.eloHalf = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.flexElo = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.flexEloPPR = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.flexEloHalf = "1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00,1500.00"
        self.url = url

    def __repr__(self):
        return "" + str(self.name) + "," + str(self.position) + "," + str(self.team)