from flask import Flask, render_template, url_for, redirect
#pip install RPI.GPIO
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

led_pin_dict = {'red': 21}
GPIO.setup(led_pin_dict['red'], GPIO.OUT)
led_state_dict = {'red':0}

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html', led_state_dict= led_state_dict)

@app.route('/<color>/<int:state>')
def LED_control(color, state):
    led_state_dict[color]= state
    
    GPIO.output(led_pin_dict['red'], led_state_dict['red'])
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
