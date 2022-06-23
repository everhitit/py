from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app= Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])    
def data():
    data = request.form['led']

    if(data == 'on'):
        GPIO.output(ledPin, 1)  # LED 켜줌
        return home()
    elif(data == 'off'):
        GPIO.output(ledPin, 0)  # LED 끔
        return home()
    elif(data == 'clean'):     # GPIO를 cleanup으로 초기화
        GPIO.cleanup()
        return home()
    elif(data == 'restart'):   # clean 이후에 다시 LED를 제어하고싶을때 GPIO를 다시 세팅
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ledPin, GPIO.OUT)
            return home()
        except:
            print("이미 핀이 설정되있습니다")
            return home()

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '8090')
