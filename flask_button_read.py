from flask import Flask, render_template
#pip install RPI.GPIO
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

sw_pin_list = [17]
GPIO.setup(sw_pin_list[0], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

sw_state_list=[0]

app=Flask(__name__)

@app.route('/')
def home():
    for ii in range(1):
        sw_state_list[ii] = GPIO.input(sw_pin_list[ii])
    return render_template('index3.html', sw_state_list= sw_state_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
