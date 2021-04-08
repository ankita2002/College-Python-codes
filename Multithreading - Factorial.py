# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:10:53 2021

@author: Ankita Upadhyay
"""

#Multithreading
#1.Calulate factorial using recursion
#2.Calulate factorial using thread

from _thread import start_new_thread
from time import sleep

threadId = 1 #counter
waiting = 2 #2sec

def factorial(n):
    global threadId
    rc = 0
    
    if n<1 : #base case
        print("{}:{}".format('\n Thread', threadId))
        threadId += 1
        rc = 1
    else :
        returnNumber = n *  factorial( n-1 ) #recursive call
        print("{} != {}".format(str(n),str(returnNumber)))
        rc = returnNumber
    return rc

start_new_thread(factorial, (5,))
start_new_thread(factorial, (4,))

print("Waiting for treads to return...")