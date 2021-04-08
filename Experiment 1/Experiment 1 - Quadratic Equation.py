# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:26:03 2021

@author: Ankita Upadhyay
"""

import math
a = int(input("Enter coefficient of a: "))
b = int(input("Enter coefficient of b: "))
c = int(input("Enter coefficient of c: "))
descriminent = b*b-4*a*c
val = math.sqrt(abs(descriminent))  
if(descriminent>0):
    print("Roots are Real and distinct")
    print("Root 1: ",(-b + val)/(2 * a))  
    print("Root 2: ",(-b - val)/(2 * a))   
elif(descriminent==0):
    print("Roots are Real and equal")
    print("Root 1 = Root 2:",-b / (2 * a))
elif (descriminent<0):
    print("Roots are complex")
    print("Root 1: ",- b / (2 * a), " + i", val)
    print("Root 1: ",- b / (2 * a), " - i", val)    

    