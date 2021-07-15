import Adafruit_DHT import time
import requests import serial
import string
import pynmea2
KEY = 'KEY'
# write the function to upload data to thingspeak
def pushData1(temp:float, humidity:float):
    url = 'https://api.thingspeak.com/update'
    params = {'key': KEY, 'field1': temp, 'field2': humidity}
    res = requests.get(url, params=params)
# define the sensor and pin/out
sensor=Adafruit_DHT.DHT11
gpio=4
while True:
    # read data from HX711 sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print(“Next test”)
    # upload data to thingspeak
    pushData1(temperature,humidity)
    time.sleep(60)
