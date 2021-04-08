# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:17:46 2021

@author: Ankita Upadhyay
"""

import time
import threading

def square(numbers):
    print("calculate square numbers:")
    for i in numbers:
        time.sleep(2) #artificial time delay
        print('square:', str(i*i))
        
def cube(numbers):
    print("Calculate cube numbers: ")
    for i in numbers:
        print('cube: ', str(i*i*i))
        
if __name__ == '__main__':
    arr = [2,3,8,9]
    
    t1 = threading.Thread(target = square,args=(arr,))
    t2 = threading.Thread(target = cube, args=(arr,))
    t1.start()
    t2.start()
    t1.join(25)
    t2.join()
    
    print("successes")