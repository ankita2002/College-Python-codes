# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:35:04 2021

@author: Ankita Upadhyay
"""
a = int(input("Enter lower range: ")) 
b = int(input("Enter upper range: "))
if a<b :
    for i in range(a,b+1):
        c=0
        for j in range(1,i+1):
            if(i%j==0):
                c=c+1
        if(c==2):
            print(i)
        