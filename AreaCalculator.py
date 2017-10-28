""" it is a calculator that can
compute the area of a given shape 
selected by the user
will be able to determine area of triangle or circle
depending on the shape selected
can calculate the area of shape and print it
"""
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print "The calculator is starting now! Let's party begin!"
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Don't forget to include the correct units! \nExiting..."
option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()
if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = pi * radius ** 2
  print "The pie is baking..."
  sleep(1)
  print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  areat = 0.5 * base * height
  print "One , two, three.."
  sleep(1)
  print ("Area: %.2f. \n%s" % (areat, hint))
else: 
  print "Error! Invalis shape selector specified. Exiting."
  
