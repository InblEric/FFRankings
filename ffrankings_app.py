from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')
    
@app.route('/about')
def about():
    session['voted'] = False
    return render_template('about.html')

@app.route('/rankings')
def rankings():
    session['voted'] = False
    return render_template('rankings.html')
    
@app.route('/matchups/<num>')
def matchup(num):
    session['voted'] = False
    return render_template('matchup.html', num=num)
    #return "this is the page for matchup number " + str(num)


@app.route('/voted', methods=['POST'])
def voted():
    session['voted'] = False
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
            session['voted'] = True
            session['choice'] = 1
            return redirect(url_for('hello'))
        elif request.form['value'] == "Vote2":
            session['voted'] = True
            session['choice'] = 2
            return redirect(url_for('hello'))
    return render_template('home.html')

if __name__ == "__main__":
    app.secret_key = '\x98-Y%\xfcL\xb9\xde\xa2\xf0\x829K\xac\xc3\xbe\xac\x0e\xe8\xb0\ni\x92\xb6'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)