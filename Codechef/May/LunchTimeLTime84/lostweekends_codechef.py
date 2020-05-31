# -*- coding: utf-8 -*-
"""
Created on Sat May 30 23:11:16 2020

@author: noell
"""

#for i in range(int(input())):
    #A = map(int, input().split())

for i in range(int(input())):
    A = input().split()
    O=0
    lastindex = len(A)-1 #A is an object, convert to list for len function to work
    P=int(A[lastindex])
    for i in range(lastindex):
        O = O+int(A[i])
   
    if O*P>120:
       print('Yes')
    else:
       print('No')   