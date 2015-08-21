from flask import Flask, render_template, request, redirect, url_for
from models.player import Player
from models.player import db
import datetime
import os
import traceback
import random
import sys

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
    qbs.sort(key=lambda x: x.name)
    rbs.sort(key=lambda x: x.name)
    wrs.sort(key=lambda x: x.name)
    tes.sort(key=lambda x: x.name)
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
    return render_template('rankings.html')

def get_player_for_matchup(position):
    if position == "Flex":
        pass
        #Player.query.filter(position != "QB")
        #flex, pick random players not QB
    else:
        pass
        #pick two random players of specific position
    # for now do this:
    with app.app_context():
        qbs = Player.query.filter_by(position="QB")
    qbs = list(qbs.all())
    qbs.sort(key=lambda x: x.name)
    return qbs[2], qbs[3]


@app.route('/matchups/<pos>/<scoring>')
def matchup(pos, scoring):
    all = False
    needScoring = True
    if str(pos) == "all":
        all = True
        options = ["qb", "rb", "wr", "te", "flex"]
        pos = random.choice(options)

    if str(pos) == "qb":
        needScoring = False

    #HOW DO I GET THE SCORING???

    player1, player2 = get_player_for_matchup(pos)

    #store/log hit to this endpoint for stats
    week = get_fantasy_week()
    return render_template('matchup.html', week=week, pos=str(pos).upper(), player1=player1, player2=player2, all=all, scoring=scoring, needScoring=needScoring)
    #return render_template('matchup.html', num=num, player1url = player1url)
    #return "this is the page for matchup number " + str(num)


@app.route('/voted', methods=['POST'])
def voted():
    #store/log hit to this endpoint for stats



    player1 = str(request.form.get('player1'))
    player2 = str(request.form.get('player2'))
    position = str(request.form.get('Position'))
    week = str(get_fantasy_week())
    scoring = str(request.form.get('scoring'))
    needScoring = str(request.form.get('needScoring')) == "True"


    print "Scoring: " + scoring
    print "need? " + str(needScoring)
    if not needScoring:
        print "QB, no scoring format."

    if str(request.form.get('all')) == "True":
        print "came here from all"
        # redirect to matchups/all
    else:
        print "came from " + str(position)
        # redirect to matchups/pos


    if request.form.get('value1', None):
        print "Voted for " + player1 + " over " + player2 + " for " + position + " in week " + week
        return redirect(url_for('hello'))



    elif request.form.get('value2', None):
        print "Voted for " + player2 + " over " + player1 + " for " + position + " in week " + week
        return redirect(url_for('hello'))

    # grab the results, compute ELO changes, and save them
    # need to scoring format

    # then, either send them back to a random vote page or make then navigate themselves




    return render_template('home.html')

if __name__ == "__main__":
    app.secret_key = '\x98-Y%\xfcL\xb9\xde\xa2\xf0\x829K\xac\xc3\xbe\xac\x0e\xe8\xb0\ni\x92\xb6'

    app.run(debug=True)