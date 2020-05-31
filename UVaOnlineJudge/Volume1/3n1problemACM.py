# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:23:59 2020

@author: noell
"""
def function (x):
    i =1
    while x>1:
        if x%2==0:
            x=x/2
        else:
            x=3*x+1
        i = i+1
    return i
        
i = int(input())
k = int(input())
cycle = []

for n in range (i, k+1):
    cycle.append(function(n))
    maxcycle = cycle
for m in range (len(cycle)):
    if m ==0:
       maxcycle = cycle[m]
    if m >0 and cycle[m]>maxcycle:
       maxcycle = cycle[m]
print(maxcycle)