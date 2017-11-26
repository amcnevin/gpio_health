#import the GPIO package
import RPi.GPIO as GPIO
import sys
import requests

# Define Pins
GREEN=7
RED=11
YELLOW=13

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

# url from cli
URL = sys.argv[1]

# HTTP GET of url
r = requests.get(url=URL)

# read JSON
data = r.json();

# strip out overall status
status = data["status"]["status"]

# Toggle LEDs
if status == "UP":
    GPIO.output(GREEN,True)
    GPIO.output(RED,False)
    GPIO.output(YELLOW,False)
elif status == "DOWN":
    GPIO.output(GREEN,False)
    GPIO.output(RED,True)
    GPIO.output(YELLOW,False)
else:
    GPIO.output(GREEN,False)
    GPIO.output(RED,False)
    GPIO.output(YELLOW,True)



