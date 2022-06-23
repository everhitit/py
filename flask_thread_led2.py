from flask import Flask, render_template, url_for, redirect
#pip install RPI.GPIO
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)

led_pin_dict = {'red': 21}
GPIO.setup(led_pin_dict['red'], GPIO.OUT)
thread_state={'red':0}

app=Flask(__name__)

# 외부 변수인 thread_state의 값이 1이면 LED를 3초 켜주고 끔
# 꺼주고 난뒤 therad_state를 0으로 만들어주고 다시 켜지않음
# 다시켜려면 웹에서 thread_state를 1로 만들어줘야함.
# Flask 프로그램 수행동안 계속 수행되고 있음. while True를 통해.
# 스레드로 수행되었으므로, 여러개 만들어 수행할 수 있음.
def LED_blink_core():
    past_time=int(time.time())
    led_state_dict={'red':0}
    while True:
        current_time=int(time.time())
        if current_time - past_time > 1:
            for color_idx in ['red']:
                led_state_dict[color_idx] = not led_state_dict[color_idx]
                if thread_state[color_idx]:
                    GPIO.output(led_pin_dict[color_idx], led_state_dict[color_idx])
            past_time = current_time        
        
# 스레드 만듬, 백그라운드에서 계속 돌릴것임.
thread1 = threading.Thread(target=LED_blink_core, args=())
thread1.start();

@app.route('/')
def home():
    return render_template('index5.html')

# 무조건 켜고 끄기 LED
@app.route('/<color>/<int:state>')
def LED_control(color, state):
    thread_state[color]= state
    GPIO.output(led_pin_dict[color], state)
    return redirect(url_for('home'))

# 3초간 켜고 끄기 위해
@app.route('/<color>')
def LED_blink(color):
    thread_state[color]= True
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090")
