from ffrankings_app import app
from ffrankings_app import db
from ffrankings_app import Player
from ffrankings_app import Week

import nflgame
with app.app_context():
    db.drop_all()
    db.create_all()

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

    for i in range(1,18):
        w = Week(i)
        db.session.add(w)

    db.session.commit()