from ffrankings_app import app
from ffrankings_app import db
from ffrankings_app import Player
import nflgame
with app.app_context():
    Player.query.delete()

QBs = []
RBs = []
WRs = []
TEs = []
with app.app_context():
    for p in nflgame.players.itervalues():
        if p.position == 'QB':
            player = Player(p.name, p.position, p.team, p.profile_url)
            db.session.add(player)
        elif p.position == 'RB':
            player = Player(p.name, p.position, p.team, p.profile_url)
            db.session.add(player)        
        elif p.position == 'WR':
            player = Player(p.name, p.position, p.team, p.profile_url)
            db.session.add(player)        
        elif p.position == 'TE':
            player = Player(p.name, p.position, p.team, p.profile_url)
            db.session.add(player)
    db.session.commit()