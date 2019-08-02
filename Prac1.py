#!/usr/bin/python3"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Dougen Hall
Student Number: HLLDOU001
Prac: 1
Date: 30/07/2019

# import Relevant Librares
import RPi.GPIO as GPIO
import time
# Logic that you write

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    LED_pins = [11, 13, 15]     #array of output LED pins
    switch_pins = [16, 18]     #array of input switch pins
    GPIO.setup(LED_pins, GPIO.OUT, initial = GPIO.LOW)     #set LED GPIO pins to output and low
    GPIO.setup(switch_pins, GPIO.IN, pull_up_down = GPIO.PUD_UP)     #set all switch GPIO pins to inputs, make sure not floating
    GPIO.add_event_detect(16, GPIO.FALLING, callback = add, bouncetime = 300)   #set up falling edge interupt detection
    GPIO.add_event_detect(18, GPIO.FALLING, callback = subtract, bouncetime = 300)

def add(channel):     #adds one to value when add button is pressed
    global num
    if (num<=6):
        num+=1
    else:
        num = 0
    binaryCounter()

def subtract(channel):      #subtracts one from value when subtract button is pressed
    global num
    if (num>=1):
        num-=1
    else:
        num = 7
    binaryCounter()

def binaryCounter():
    global num
    binaryString = bin(num)[2:].zfill(3)
    if GPIO.input(11)!=int(binaryString[2:]):
        GPIO.output(11, not(GPIO.input(11)))
    if GPIO.input(13)!=int(binaryString[1:2]):
        GPIO.output(13, not(GPIO.input(13)))
    if GPIO.input(15)!=int(binaryString[0:1]):
        GPIO.output(15, not(GPIO.input(15)))


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        num = 0
        main()
        while True: #will continue loop
            time.sleep(200) #delay of 200mS
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
   # except e:
       # GPIO.cleanup()
       # print("Some other error occurred")
       # print(e.message)