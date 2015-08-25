from ffrankings_app import app
from ffrankings_app import db
from ffrankings_app import Player
from models.player import get_fantasy_week

def lookupRank(pos, fname, lname):
    if pos == "QB":
        with open('QBR.txt') as file:
            for line in file:
                if fname in line and lname in line:
                    return int(line[0:3])
    elif pos == "RB":
        with open('RBR.txt') as file:
            for line in file:
                if fname in line and lname in line:
                    return int(line[0:3])
    elif pos == "WR":
        with open('WRR.txt') as file:
            for line in file:
                if fname in line and lname in line:
                    return int(line[0:3])
    elif pos == "TE":
        with open('TER.txt') as file:
            for line in file:
                if fname in line and lname in line:
                    return int(line[0:3])
    return -1




count = 0
ranks = []
with app.app_context():
    p = Player.query.filter(Player.position == "QB")
    for i in p:
        print i
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        print rank
        print "\n\n"
        if rank != -1:
            ranks.append(int(rank))
        count += 1
    for i in p:
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        if rank != -1:
            print str(i) + " rank= " + str(rank)
            elo = 1800 - ((600.0/(count-1)) * (rank - 1))
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
        else:
            print str(i) + " rank= " + str(rank)
            elo = 1100
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
    db.session.commit()

count = 0
ranks = []
with app.app_context():
    p = Player.query.filter(Player.position == "RB")
    for i in p:
        print i
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        print rank
        print "\n\n"
        if rank != -1:
            ranks.append(int(rank))
        count += 1
    for i in p:
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        if rank != -1:
            print str(i) + " rank= " + str(rank)
            elo = 1800 - ((600.0/(count-1)) * (rank - 1))
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
        else:
            print str(i) + " rank= " + str(rank)
            elo = 1100
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
    db.session.commit()

count = 0
ranks = []
with app.app_context():
    p = Player.query.filter(Player.position == "WR")
    for i in p:
        print i
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        print rank
        print "\n\n"
        if rank != -1:
            ranks.append(int(rank))
        count += 1
    for i in p:
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        if rank != -1:
            print str(i) + " rank= " + str(rank)
            elo = 1800 - ((600.0/(count-1)) * (rank - 1))
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
        else:
            print str(i) + " rank= " + str(rank)
            elo = 1100
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
    db.session.commit()

count = 0
ranks = []
with app.app_context():
    p = Player.query.filter(Player.position == "TE")
    for i in p:
        print i
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        print rank
        print "\n\n"
        if rank != -1:
            ranks.append(int(rank))
        count += 1
    for i in p:
        rank = lookupRank(i.position, i.name.split(" ")[0], i.name.split(" ")[1])
        if rank != -1:
            print str(i) + " rank= " + str(rank)
            elo = 1800 - ((600.0/(count-1)) * (rank - 1))
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
        else:
            print str(i) + " rank= " + str(rank)
            elo = 1100
            print "elo = " + str(elo)
            elo_arr = i.elo.split(",")
            week = get_fantasy_week()
            elo_arr[week-1] = str("%.2f" % elo)
            i.elo = str(elo_arr).strip("[]").replace("'", "").replace(" ", "")
    db.session.commit()




#all = range(1,76)
#print all
#print "\n\n"
#print ranks
#print "\n\n"
#print list(set(all) - set(ranks))