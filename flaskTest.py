#pip install flask
from flask import Flask 
#pip install RPI.GPIO
import RPi.GPIO as GPIO

app=Flask(__name__)

ledPin=21

@app.route('/')
def flask():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, 0)
    return 'Hello Flask'


@app.route('/led/on')
def ledOn():
    GPIO.output(ledPin, 1)
    return '<h1> LED ON </h1>'

@app.route('/led/off')
def ledOff():
    GPIO.output(ledPin, 0)
    return '<h1> LED OFF </h1>'

@app.route('/led/clean')
def clean():
    GPIO.cleanup()
    return '<h1> GPIO Clean </h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
