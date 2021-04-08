# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:49:32 2021

@author: Ankita Upadhyay
"""

n=float(input("Enter a number: "))
if n >=0:
    if(n==0):
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")
if(n%2==0):
    print("{0} is a Even Number".format(n))
else:
    print("{0} is an Odd Numb-er".format(n))    