#!/usr/bin/env python
# encoding: utf-8
"""
send_request.py

Created by Chris Mitchell on 2018-06-12.
"""

import json
import urllib.request
from time import sleep
import pifacedigitalio as p
p.init()

def turn_right():
   p.digital_write(2,1)
   p.digital_write(3,1)
   sleep(0.25)
   p.digital_write(2,0)
   p.digital_write(3,0)

def turn_left():
   p.digital_write(1,1)
   p.digital_write(4,1)
   sleep(0.25)
   p.digital_write(1,0)
   p.digital_write(4,0)

def go_forward():
   p.digital_write(2,1)
   p.digital_write(4,1)
   sleep(0.5)
   p.digital_write(2,0)
   p.digital_write(4,0)

def go_backward():
   p.digital_write(1,1)
   p.digital_write(3,1)
   sleep(0.5)

def stay():
    p.digital_write(1,0)
    p.digital_write(2,0)
    p.digital_write(3,0)
    p.digital_write(4,0)
	
def run_command(command):
   if(command == 'right'):
      turn_right()
   elif(command == 'left'):
      turn_left()
   elif(command == 'forward'):
      go_forward()
   elif(command == 'backward'):
      go_backward()
   elif(command == 'stay'):
      stay()


while True:
        #response = urllib.request.urlopen('https://mechaian-207101.appspot.com/i$
        response = urllib.request.urlopen('https://rover-jmmmd.appspot.com/instru$
        response_byte = response.read()
        response_str = response_byte.decode()
        print(response_str)
        response_obj = json.loads(response_str)
        command = response_obj['command']
        print(command)
        run_command(command)
        sleep(0.5)