from flask import Flask 
#pip install RPI.GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

ledPin=21
GPIO.setup(ledPin, GPIO.OUT)

app=Flask(__name__)

@app.route('/')
def flask():
    return '<h1> LED Control WebPage </h1>'


@app.route('/led/<state>')
def led(state):
    if(state == 'on'):
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

    return ('<h1> LED %s </h1>' % state)

@app.route('/led/clean')
def clean():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()
    return '<h1> GPIO Clean </h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
