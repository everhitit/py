import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 핀들의 번호를 지정하는 규칙 설정

LED_pin = 21
GPIO.setup(LED_pin, GPIO.OUT)
pwm = GPIO.PWM(LED_pin, 1000) # LED 핀에 1000Hz의 PWM 설정
pwm.start(0) # 처음 PWM 출력은 0으로 설정

try:
    while True:
        pwm.ChangeDutyCycle(0) # 값은 %임. 0~100
        time.sleep(1)          # 1초 대기
        pwm.ChangeDutyCycle(25)
        time.sleep(1)
        pwm.ChangeDutyCycle(50)
        time.sleep(1)
        pwm.ChangeDutyCycle(75)
        time.sleep(1)
        pwm.ChangeDutyCycle(100)
        time.sleep(1)

# 반드시 있어야함.    
finally:
    GPIO.cleanup() # GPIO핀들을 초기화함.
    