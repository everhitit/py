import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO 핀들의 번호를 지정하는 규칙 설정

LED_pin = 21
sw_pin=17
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# 스위치 핀을 풀다운 저항이 있는 출력으로 설정
# 풀다운 저항이 있으면 버튼을 누리지 않으면 LOW 신호가 됨
# 여기를 GPIO.PUD_UP으로 하면 버튼을 누르지 않으면 HIGH신호가 됨


try:
    while True:
        if GPIO.input(sw_pin) == GPIO.HIGH:
            GPIO.output(LED_pin, GPIO.HIGH)
        else:
            GPIO.output(LED_pin, GPIO.LOW)
        


# 반드시 있어야함.    
finally:
    GPIO.cleanup() # GPIO핀들을 초기화함.
    