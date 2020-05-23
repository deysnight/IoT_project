
from flask import Flask, url_for, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sensors')
def config():
    
    res = random.uniform(1, 10)
    
    return str('{"dig": "day", "ana": ' + str(res) + '}')
