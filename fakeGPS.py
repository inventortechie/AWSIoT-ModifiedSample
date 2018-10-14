#!/usr/bin/env python3
# encoding: utf-8

import random

# Outputs Random Address from Defined List
def myStreet():
    addy1 = "95085 Florencio Lights, XYZ, AB"
    addy2 = "76229 Eveline Pass, XYZ, AB"
    addy3 = "253 Johnson Creek, XYZ, AB"
    addy4 = "15275 Elfrieda Street, XYZ, AB"
    addy5 = "3242 Bethany Loop, XYZ, AB"
    choice = random.choice((addy1,addy2,addy3,addy4,addy5))
    return choice

# Generate Fake GPS Coordinates.
def myCoords():
    x = round(random.uniform(-180,180), 4)
    y = round(random.uniform(-180,180), 4)
    return x,y

print(myCoords())
print(myStreet())
