#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:15:12 2019

@author: andres

https://www.guru99.com/reading-and-writing-files-in-python.html

"""

f=open("test_gcode.txt", "r")
if f.mode == 'r':
    contents =f.read()
lines = contents.splitlines()
cartesian = ['X','Y','Z','G92',';']
moving = ['X','Y','Z']
no_extruder = []
has_fan = []
for line in lines:
    if (not ((not any(x in line for x in cartesian)) and ('E' in line)) and line!= "M106"):
        no_extruder.append(line)  
for line in no_extruder:
    if('E0' in line):
       has_fan.append(line.replace(" E0",""))
    elif('E' in line and any(x in line for x in moving)):
       has_fan.append("M106 S255")
       code, e, trash= line.partition('E')
       has_fan.append(code)
    else:
        if any(x in line for x in moving):
            has_fan.append("M107")
            has_fan.append(line)
        else:
            has_fan.append(line)
print(has_fan)
new_gcode = '\n'.join(has_fan)
text_file = open("Output.gcode", "w")
text_file.write(new_gcode)
text_file.close()


        
        
            
