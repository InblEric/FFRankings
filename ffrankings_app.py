from flask import Flask, render_template, request, redirect, url_for
from models.player import Player
from models.player import db
import datetime
import os
import traceback
import random
import sys
import math

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


# later on
db.init_app(app)


week1start = datetime.date(2015, 9, 8)
week1end = datetime.date(2015, 9, 14)

def get_fantasy_week(today=datetime.date.today()):
    weekend = week1end
    week = 1
    while weekend < today:
        weekend = weekend + datetime.timedelta(days=7)
        week += 1
    return week






emptyPlayer = Player("No more players", "...", "...", "")

@app.route('/')
def hello():
    #store/log hit to this endpoint for stats
    #players = []
    with app.app_context():
        qbs = Player.query.filter_by(position="QB")
        rbs = Player.query.filter_by(position="RB")
        wrs = Player.query.filter_by(position="WR")
        tes = Player.query.filter_by(position="TE")
    qblist = [emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer]
    rblist = [emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer]
    wrlist = [emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer]
    telist = [emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer, emptyPlayer]
    qbs = list(qbs.all())
    rbs = list(rbs.all())
    wrs = list(wrs.all())
    tes = list(tes.all())
    qbs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    rbs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    wrs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    tes.sort(key=lambda x: x.get_week_elo(), reverse=True)

    #SORT BY ELO BEFORE SENDING
    #TO TEMPLATE
    #WE CAN LIMIT IT TO 5 HERE TO SAVE TIME FOR HOMEPAGE

    count = 0
    for qb in qbs:
        qblist[count] = qb
        count += 1
        if count == 5:
            break
    count = 0
    for rb in rbs:
        rblist[count] = rb
        count += 1
        if count == 5:
            break
    count = 0
    for wr in wrs:
        wrlist[count] = wr
        count += 1
        if count == 5:
            break
    count = 0
    for te in tes:
        telist[count] = te
        count += 1
        if count == 5:
            break
    return render_template('home.html', qbs = qblist, rbs = rblist, wrs = wrlist, tes = telist)
    
@app.route('/about')
def about():
    print "in about"
    #store/log hit to this endpoint for stats
    print "rendering..."
    return render_template('about.html')

@app.route('/rankings')
def rankings():
    #store/log hit to this endpoint for stats
    #players = []
    with app.app_context():
        qbs = Player.query.filter_by(position="QB")
        rbs = Player.query.filter_by(position="RB")
        wrs = Player.query.filter_by(position="WR")
        tes = Player.query.filter_by(position="TE")
    qbs = list(qbs.all())
    rbs = list(rbs.all())
    wrs = list(wrs.all())
    tes = list(tes.all())
    qbs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    rbs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    wrs.sort(key=lambda x: x.get_week_elo(), reverse=True)
    tes.sort(key=lambda x: x.get_week_elo(), reverse=True)
    #store/log hit to this endpoint for stats
    return render_template('rankings.html', qbs=qbs, rbs=rbs, wrs=wrs, tes=tes)

def get_player_for_matchup(position):
    if position == "flex":
        with app.app_context():
            players = Player.query.filter(position != "QB")
            players = list(players.all())
        random.shuffle(players)

        player1 = players[0]
        player2 = players[1]
        next = 2
        while player1.position == "QB":
            player1 = players[next]
            next += 1
        while player2.position == "QB":
            player2 = players[next]
            next += 1



    else:
        with app.app_context():
            players = Player.query.filter_by(position=position.upper())
            players= list(players.all())
        random.shuffle(players)



        player1 = players[0]
        player2 = players[1]

    return player1, player2


@app.route('/matchups/<pos>/<scoring>')
def matchup(pos, scoring):
    needScoring = True
    all = False
    if str(pos) == "all":
        all = True
        options = ["qb", "rb", "wr", "te", "flex"]
        pos = random.choice(options)
    if str(scoring) == "Half":
        scoring = "0.5 PPR"
    if pos.upper() == "QB":
        needScoring = False
    player1, player2 = get_player_for_matchup(pos)

    #store/log hit to this endpoint for stats
    week = get_fantasy_week()
    return render_template('matchup.html', week=week, pos=str(pos).upper(), player1=player1, player2=player2, all=all, scoring=scoring, needScoring=needScoring)

def k(elo):
    ans = 116 - (0.04076923076923 * (elo-100))
    return ans

def get_new_elos(winner_elo, loser_elo):

    week = get_fantasy_week()
    winner_elo_arr = winner_elo.split(",")
    loser_elo_arr = loser_elo.split(",")
    i = 0
    for rating in winner_elo_arr:
        winner_elo_arr[i] = str(winner_elo_arr[i])
        i += 1
    i = 0
    for rating in loser_elo_arr:
        loser_elo_arr[i] = str(loser_elo_arr[i])
        i += 1


    winner_elo_week = float((winner_elo.split(","))[week-1])
    loser_elo_week = float((loser_elo.split(","))[week-1])

    qa = math.pow(10, (winner_elo_week/400))
    qb = math.pow(10, (loser_elo_week/400))

    winner_expected_score = qa / (qa + qb)
    loser_expected_score = qb / (qa + qb)

    new_winner_elo_week = winner_elo_week + k(winner_elo_week) * (1 - winner_expected_score)
    new_loser_elo_week = loser_elo_week + k(loser_elo_week) * (0 - loser_expected_score)

    winner_elo_arr[week-1] = str("%.2f" % new_winner_elo_week)
    loser_elo_arr[week-1] = str("%.2f" % new_loser_elo_week)

    new_winner_elo = str(winner_elo_arr).strip("[]").replace("'", "").replace(" ", "")
    new_loser_elo = str(loser_elo_arr).strip("[]").replace("'", "").replace(" ", "")

    return new_winner_elo, new_loser_elo


@app.route('/voted', methods=['POST'])
def voted():
    #store/log hit to this endpoint for stats
    p1lookup = str(request.form.get('player1')).split(",")
    p2lookup = str(request.form.get('player2')).split(",")
    position = str(request.form.get('Position'))
    week = str(get_fantasy_week())
    scoring = str(request.form.get('scoring'))
    winner = 0
    if scoring == "0.5 PPR":
        scoring = "Half"
    if request.form.get('value1', None):
        winner = 1
    elif request.form.get('value2', None):
        winner = 2
    else:
        print "wat"

    with app.app_context():
        p1 = Player.query.filter(Player.name == p1lookup[0]).filter(Player.position == p1lookup[1]).filter(Player.team == p1lookup[2]).first()
        p2 = Player.query.filter(Player.name == p2lookup[0]).filter(Player.position == p2lookup[1]).filter(Player.team == p2lookup[2]).first()
        #p1 = list(p1.all())[0]
        #p2 = list(p2.all())[0]

        if position.upper() == "QB":
            print "QB, no scoring format."

            if winner == 1:
                newElo1, newElo2 = get_new_elos(p1.elo, p2.elo)
                with app.app_context():
                    p1.elo = newElo1
                    p2.elo = newElo2
                    db.session.commit()
            if winner == 2:
                newElo2, newElo1 = get_new_elos(p2.elo, p1.elo)
                with app.app_context():
                    p1.elo = newElo1
                    p2.elo = newElo2
                    db.session.commit()

        # options = ["qb", "rb", "wr", "te", "flex"]

        elif position == "flex":
            if scoring == "Standard":
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.flexElo, p2.flexElo)
                    with app.app_context():
                        p1.flexElo = newElo1
                        p2.flexElo = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.flexElo, p1.flexElo)
                    with app.app_context():
                        p1.flexElo = newElo1
                        p2.flexElo = newElo2
                        db.session.commit()
            elif scoring == "PPR":
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.flexEloPPR, p2.flexEloPPR)
                    with app.app_context():
                        p1.flexEloPPR = newElo1
                        p2.flexEloPPR = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.flexEloPPR, p1.flexEloPPR)
                    with app.app_context():
                        p1.flexEloPPR = newElo1
                        p2.flexEloPPR = newElo2
                        db.session.commit()
            elif scoring == "Half":
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.flexEloHalf, p2.flexEloHalf)
                    with app.app_context():
                        p1.flexEloHalf = newElo1
                        p2.flexEloHalf = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.flexEloHalf, p1.flexEloHalf)
                    with app.app_context():
                        p1.flexEloHalf = newElo1
                        p2.flexEloHalf = newElo2
                        db.session.commit()
        else:
            if scoring == "Standard":
                print "checking..."
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.elo, p2.elo)
                    with app.app_context():
                        p1.elo = newElo1
                        p2.elo = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.elo, p1.elo)
                    with app.app_context():
                        p1.elo = newElo1
                        p2.elo = newElo2
                        db.session.commit()
            elif scoring == "PPR":
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.eloPPR, p2.eloPPR)
                    with app.app_context():
                        p1.eloPPR = newElo1
                        p2.eloPPR = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.eloPPR, p1.eloPPR)
                    with app.app_context():
                        p1.eloPPR = newElo1
                        p2.eloPPR = newElo2
                        db.session.commit()
            elif scoring == "Half":
                if winner == 1:
                    newElo1, newElo2 = get_new_elos(p1.eloHalf, p2.eloHalf)
                    with app.app_context():
                        p1.eloHalf = newElo1
                        p2.eloHalf = newElo2
                        db.session.commit()
                if winner == 2:
                    newElo2, newElo1 = get_new_elos(p2.eloHalf, p1.eloHalf)
                    with app.app_context():
                        p1.eloHalf = newElo1
                        p2.eloHalf = newElo2
                        db.session.commit()


    if str(request.form.get('all')) == "True":
        print "came here from all"
        # redirect to matchups/all




        #return redirect(url_for('matchup'), pos="all", scoring=scoring)
        #return redirect(url_for('matchups/qb/standard'))
        #return redirect(url_for('matchup/all/' + scoring))
    else:
        print "came from " + str(position)
        # redirect to matchups/pos
        #return redirect(url_for('matchups/' + str(position) + "/" + scoring))

    if winner == 1:
        print "Voted for " + str(p1lookup[0]) + " over " + str(p2lookup[0]) + " for " + position + " in week " + week
        return redirect(url_for('hello'))
    elif winner == 2:
        print "Voted for " + str(p2lookup[0]) + " over " + str(p1lookup[0]) + " for " + position + " in week " + week
        return redirect(url_for('hello'))
    return render_template('home.html')

if __name__ == "__main__":
    app.secret_key = '\x98-Y%\xfcL\xb9\xde\xa2\xf0\x829K\xac\xc3\xbe\xac\x0e\xe8\xb0\ni\x92\xb6'
    app.run(debug=True)