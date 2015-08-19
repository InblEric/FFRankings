from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import time

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'hello'
    return render_template('home.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rankings')
def rankings():
    return render_template('rankings.html')
    
@app.route('/matchups/<num>')
def matchup(num):
    return render_template('matchup.html', num=num)
    #return "this is the page for matchup number " + str(num)


@app.route('/voted', methods=['POST'])
def voted():
    email = None
    if request.method == 'POST':
        #email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        #if not db.session.query(User).filter(User.email == email).count():
        #    reg = User(email)
        #    db.session.add(reg)
        #    db.session.commit()


        #actually, we want to check the contents of the POST request for the voting results
        #grab the results, compute ELO changes, and save them

        #then, either send them back to a random vote page or make then navigate themselves

        if request.form['value'] == "Vote1":
            return render_template('home.html', voted = True, choice = 1)
        elif request.form['value'] == "Vote2":
            return render_template('home.html', voted = True, choice = 2)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)