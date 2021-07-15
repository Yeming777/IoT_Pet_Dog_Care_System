import RPi.GPIO as GPIO
import time
import requests
import json
#set up pin/out diagram in rasp pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#get the key and url from thingspeak
KEY='KEY' url='url' params = {'key': KEY}
while True:
  #read data from thingspeak and reshape it to get the useable data
  res = requests.get(url, params=params).json() field_1=res['feeds']
  #collect the last input data
  index=len(field_1)-1
  temp=field_1[index]
  #based on the last entry data to determain the on/off of the LED
  i=temp['field1'] print(i)
  if i=='0':
    GPIO.output(18,GPIO.LOW) 
  else:
    GPIO.output(18,GPIO.HIGH)
