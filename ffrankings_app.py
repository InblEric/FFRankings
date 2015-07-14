from flask import Flask
from flask import render_template
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

if __name__ == "__main__":
    app.run()