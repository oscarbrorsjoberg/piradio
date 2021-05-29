#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time

VOLUME_MAX = 70
VOLUME_MIN = 0

volume = 45

def setVolume() -> None:
    subprocess.call(['amixer', 'set', 'Master', f'{volume}%'], shell=False)
    time.sleep(0.5)

def decVolume(channel) -> None:
    global volume
    volume-= 2

    if(volume < VOLUME_MIN):
        volume = VOLUME_MIN

    setVolume()

def incVolume(channel) -> None:
    global volume
    volume+= 2

    if(volume > VOLUME_MAX):
        volume = VOLUME_MAX

    setVolume()


GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(25, GPIO.RISING, callback=decVolume)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.RISING, callback=incVolume)


message = input("Press enter to quit!\n");

GPIO.cleanup()

