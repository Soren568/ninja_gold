from logging import debug
import random
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'kahsjdihp98hduqn'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    # session['activity'] = []
    if request.form['chosen_button'] == 'farm':
        session['gold_received'] = random.randint(10,20)
        session['gold'] += session['gold_received']
        # session['activity'] += session['gold_received']
    elif request.form['chosen_button'] == 'cave':
        session['gold_received'] = random.randint(5,10)
        session['gold'] += session['gold_received']
        # session['activity'] += session['gold_received']
    elif request.form['chosen_button'] == 'house':
        session['gold_received'] = random.randint(2,5)
        session['gold'] += session['gold_received']
        # session['activity'] += session['gold_received']
    elif request.form['chosen_button'] == 'casino':
        session['gold_received'] = random.randint(-50,50)
        session['gold'] += session['gold_received']
    print(request.form)
    print(session['gold'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)