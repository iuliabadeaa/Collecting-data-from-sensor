from Adafruit_GPIO import *
import Adafruit_Python_DHT
import time

while True:
    time.sleep(15)
    temperature = Adafruit_Python_DHT.read_retry(Adafruit_Python_DHT.DHT11,4)
    print(temperature)