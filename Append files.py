# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:43:11 2021

@author: Ankita Upadhyay
"""

f1 = open("myFile.txt",'r')
print("Contents of file before appending: ")
print(f1.read())

f1 = open("myFile.txt",'a+')
f1.write("\n This line is appended using appending mode")
f1.close()

print("Contents of file after appending :")
f1 = open("myFile.txt",'r')
print(f1.read())
f1.close()