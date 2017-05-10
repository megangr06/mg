# import the GPIO, time, and randint
import RPi.GPIO as GPIO
from time import sleep, time
import pygame;
from random import randint

class Constellation(object):
    # use broadcom pin mode
    GPIO.setmode(GPIO.BCM)

    # create array of GPIO pins
    pins = [26, 19, 13, 6, 5, 22, 27, 17]
    # setup the output pins
    GPIO.setup(pins, GPIO.OUT)

    # initialize the constellation
    def __init__(self, name):
        self.name = name

    # off function
    def off(self):
        GPIO.output(26, False)
        GPIO.output(19, False)
        GPIO.output(13, False)
        GPIO.output(6, False)
        GPIO.output(5, False)
        GPIO.output(22, False)
        GPIO.output(27, False)
        GPIO.output(17, False)
        sleep(.3)

    # on function
    def on(self):
        GPIO.output(26, True)
        GPIO.output(19, True)
        GPIO.output(13, True)
        GPIO.output(6, True)
        GPIO.output(5, True)
        GPIO.output(22, True)
        GPIO.output(27, True)
        GPIO.output(17, True)
        
    # depending on name light LEDs a certain way
    def light(self, name):
        self.off()
        if (name == "sagittarius"):
            # turn on 4, 5, 6, 8
            GPIO.output(6, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            GPIO.output(17, True)
            sleep(3.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(3.5)
            self.off()
            # turn on 1, 2, 4, 7, 8
            GPIO.output(26, True)
            GPIO.output(19, True)
            GPIO.output(6, True)
            GPIO.output(27, True)
            GPIO.output(17, True)
            sleep(3.5)
            self.off()
            # turn on 3, 5
            GPIO.output(13, True)
            GPIO.output(5, True)
            sleep(3.5)
            self.off()
            # turn on 4
            GPIO.output(6, True)
            sleep(3.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(3.5)
            self.off()
            # turn on 2, 4, 5
            GPIO.output(19, True)
            GPIO.output(6, True)
            GPIO.output(5, True)
            sleep(3.5)
            self.off()
            # turn on 4, 6
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "virgo"):
            # turn on 5, 7
            GPIO.output(5, True)
            GPIO.output(27, True)
            sleep(3.5)
            self.off()
            # turn on 4, 6
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on 7
            GPIO.output(27, True)
            sleep(3.5)
            self.off()
            # turn on 1, 4
            GPIO.output(26, True)
            GPIO.output(6, True)
            sleep(3.5)
            self.off()
            # turn on 2, 5, 6
            GPIO.output(19, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(3.5)
            self.off()
            # turn on 2
            GPIO.output(19, True)
            sleep(3.5)
            self.off()
            # turn on 1
            GPIO.output(26, True)
            sleep(3.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "ursa"):
            # turn on 1
            GPIO.output(26, True)
            sleep(3.5)
            self.off()
            # turn on 1
            GPIO.output(26, True)
            sleep(3.5)
            self.off()
            # turn on 2, 5, 7
            GPIO.output(19, True)
            GPIO.output(5, True)
            GPIO.output(27, True)
            sleep(3.5)
            self.off()
            # turn on 3, 4, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on 4, 7
            GPIO.output(6, True)
            GPIO.output(27, True)
            sleep(3.5)
            self.off()
            # turn on 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on none
            sleep(3.5)
            self.off()
            # turn on 3, 4, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on 7
            GPIO.output(27,True)
            sleep(3.5)
            self.off()
            # turn on 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
        if (name == "orion"):
            # turn on 1, 2
            GPIO.output(26, True)
            GPIO.output(19, True)
            sleep(3.5)
            self.off()
            # turn on 1, 2
            GPIO.output(26, True)
            GPIO.output(19, True)
            sleep(3.5)
            self.off()
            # turn on 3
            GPIO.output(13, True)
            sleep(3.5)
            self.off()
            # turn on 4
            GPIO.output(6, True)
            sleep(3.5)
            self.off()
            # turn on 6, 8
            GPIO.output(22, True)
            GPIO.output(17, True)
            sleep(3.5)
            self.off()
            # turn 6
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn 3, 6
            GPIO.output(13, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # turn on 4, 8
            GPIO.output(6, True)
            GPIO.output(17, True)
            sleep(3.5)
            self.off()
            # turn on none
            sleep(3.5)
            self.off()
            # turn on 2, 7
            GPIO.output(19, True)
            GPIO.output(27, True)
            sleep(3.5)
            self.off()
            # turn on 3, 4, 5, 6
            GPIO.output(13, True)
            GPIO.output(6, True)
            GPIO.output(5, True)
            GPIO.output(22, True)
            sleep(3.5)
            self.off()
            # blink showing reset
            for i in range(3):
                self.on()
                sleep(.2)
                self.off()
                sleep(.2)
            


# create an array for constellations
const = []

try :
    while(True):
        # create the constellations
        #const.append(Constellation("sagittarius"))
        #const.append(Constellation("virgo"))
        #const.append(Constellation("ursa"))
        #const.append(Constellation("orion"))

        # choose a random constellation to make
        #x = const[randint(0,len(const)-1)]
        x = Constellation("virgo")
        x.light(x.name)
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
