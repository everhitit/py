import RPi.GPIO as GPIO
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BCM) # GPIO 핀들의 번호를 지정하는 규칙 설정

sensor_pin=4


try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, sensor_pin)
        
        if h is not None and t is not None:
            print("Temp: {0:0.1f} C  Humidity: {1:0.1f} %".format(t,h))
        else:
            print('Read error')
            
        time.sleep(1)
except KeyboardInterrupt:
    print('Terminated by Keyboard')        

# 반드시 있어야함.    
finally:
    print('End of Program')
    