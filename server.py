
from flask import Flask, url_for, render_template
import random
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DIG_PIN = 11
ANA_PIN = 13
GPIO.setup(DIG_PIN, GPIO.IN)
GPIO.setup(ANA_PIN, GPIO.IN)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sensors')
def config():
    
    res_ana = GPIO.input(ANA_PIN);
    res_dig = GPIO.input(DIG_PIN);
    
    if (res_dig):
        state = "day"
    else:
        state = "night"
    
    return str('{"dig": "' + state + '", "ana": ' + str(res_ana) + '}')
