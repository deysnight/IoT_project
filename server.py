
DEMO = False # set to True for demo with random value

from flask import Flask, url_for, render_template
import random

if not DEMO:
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
    
	if not DEMO:
		res_ana = GPIO.input(ANA_PIN);
		res_dig = GPIO.input(DIG_PIN);
	else:
		res_ana = random.uniform(0.25, 4.2)
		res_dig = 0 if res_ana < 2 else 1


	if (res_dig):
		state = "day"
	else:
		state = "night"

	return str('{"dig": "' + state + '", "ana": ' + str(round(res_ana, 3)) + ', "per": ' + str(round(res_ana * 100 / 4.2, 2)) + '}')
