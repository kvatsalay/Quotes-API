from flask import Flask, render_template
import random
import json
import requests
app = Flask(__name__)


@app.route('/quotes')
def index():
	random_val = random.randint(1,1000)
	link = ('https://thesimpsonsquoteapi.glitch.me/quotes?num=' + str(random_val))
	l = requests.get(link)
	v = json.loads(l.content)
	val = (v[0]['quote'])
	val_2 = (v[0]['character'])
	return render_template('quotes.html', val=val, val_2=val_2)


if __name__ == '__main__':
	app.run(debug=True)
