# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:25:10 2021

@author: Ankita Upadhyay
"""

for i in range(5):
    for j in range(i+1):
        print("*", end='')
    print("\r")
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end='')
    print("\r")