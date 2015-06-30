from flask import Flask, render_template
# Import the fixer
from werkzeug.contrib.fixers import ProxyFix


from access_api import get_games_won

app = Flask(__name__)      
app.wsgi_app = ProxyFix(app.wsgi_app)
summoner_name = 'uberwold'
@app.route('/')
def home():
    value = [summoner_name,get_games_won(summoner_name)]
    return render_template('index.html',value=value)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
