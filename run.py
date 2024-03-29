import os
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def selection():
	return render_template('selection.html')

@app.route('/<opp>/<main>')
def game(main,opp):
	return render_template('game.html',main=main,opp=opp)


if (__name__ == '__main__'):
	# Bind to PORT if defined, otherwise default to 80.
	port = int(os.environ.get('PORT', 80))
	app.run(host='0.0.0.0', port=port)