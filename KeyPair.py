'''

Find a pair in an array of number where the sum of two numbers is equal to the given Value K.

sample input:
5 9
1 2 3 4 5

here 5 is the lenght of array input. 9 is the value K.
The program will print YES if such a pair is found and NO if not found.

'''

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:33:24 2019

@author: inkdhakshn
"""

''' 
1. sort the list
2. get the list of items less than k
3. do the stuff

'''

import math

def getCenter(l, k):

    
    f = 0
    b = len(l)-1
    print(l)
    if k < l[f]:
        return 0
    if l[b] < k:
        return len(l) - 1
    
    while f <= b:
        c = int(math.floor((f + b)/2))
        if l[c] < k:
            f = c - 1
        elif k > l[c]:
            b = c + 1
        else:
            return c
    if (l[f] - k) < (k - l[b]):
        return f
    else:
        return b
                    
            

if '__main__' == __name__:
    n, k = input().split()
    n = int(n)
    k = int(k)
    l = input().split()
    for i in range(len(l)):
        l[i] = int(l[i])
    l.sort()
    
    center = getCenter(l, k)
    found = False
    for i in range(center+1):
        for j in range(i+1, center+1):
            if l[i] + l[j] == k:
                found = True
                break
        if found == True:
            break
    if found == True:
        print('YES')
    else:
        print('NO')
