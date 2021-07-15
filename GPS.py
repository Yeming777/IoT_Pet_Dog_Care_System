import serial
import time
import string
import pynmea2
import requests
KEY = 'KEY'
def pushData(latitude:float, longitude:float):
    #Set up request url and parameters
    url = 'https://api.thingspeak.com/update'
    params = {'key': KEY, 'field1': latitude, 'field2': longitude}
    res = requests.get(url, params=params)
while True:
    # set up raspberry pi pin/out to read data from GPS
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readlines()
    # process the GPS data
    try:
        location=newdata[0]
        location=str(location)
        split_location=location.split(',')
        if len(split_location)>5:
            latitude=split_location[3]
            longitude=split_location[5]
            if len(latitude)==10 and len(longitude)==11:
                lat=float(latitude)/100
                lon=float(longitude)/100
                # upload to thingspeak
                pushData(-lat,lon)
                print(lat,lon)
    except:
        print('Next test')
