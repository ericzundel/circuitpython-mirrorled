# circuitpython-mirrorled
A simple way to control a neopixel strip for the Infinity Mirror project.

## Infinity Mirror LED project

This is a project used as an introduction for 9th graders to programming 
with Circuit Pytyon. The project is to create an infinity mirror and this code is used
to control the lighting inside the mirror.


## Hardware setup

An infinity mirror creates the illusion of the reflection going on infinitely.  The simplest version of this is to setup two mirrors on opposite walls. The observer stands in the middle and sees an infinite number of reflections if themselves.

To make an infinity mirror, you put a mirror inside of a glass case. Then, on one side of the glass, you put one-way film so that the mirror side of the film reflects back to the mirror.  Inside the caase you put lighting so you can see through the one way glass.

The idea behind the electronics in this project is to control the lighting inside the case.

## mirrorled library
The lib directory contains a library 'mirrorled' that is just
a very simple wrapper for the neopixel library that only allows you to 
turn pixels on and off.  


## Circuit Python Version
The .mpy files in the lib/ directory are for student convenience.  They are compiled with the Circuit Python 9 release.  If you get a version mismatch, copy fresh versions from the Adafruit Circuit Python Library version for the version of Circuit Python shown in boot.out on your microprocessor.
