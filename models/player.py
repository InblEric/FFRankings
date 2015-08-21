from flask.ext.sqlalchemy import SQLAlchemy
#from ffrankings_app import app

db = SQLAlchemy()

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