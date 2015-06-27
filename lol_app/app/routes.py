from flask import Flask, render_template

from access_api import get_games_won

app = Flask(__name__)      
summoner_name = 'uberwold'
@app.route('/')
def home():
    value = [summoner_name,get_games_won(summoner_name)]
    return render_template('home.html',value=value)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
