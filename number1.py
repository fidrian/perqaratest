#!/bin/python3

import math
import os
import random
import re
import sys

def getMedian(countExp, d, mid):
    counter = 0
    position = 0
    while counter<mid:
        counter+=countExp[position]
        position+=1
    position-=1

    if counter>mid or d%2 !=0:
        return position
    else:
        return (2*position+1)/2

def activityNotifications(expenditure, d):
    countExp = [0]*201
    end = d
    
    for i in range(0,end):
        countExp[expenditure[i]]+=1
    
    notif = 0
    
    if d%2==0:
        mid = int(d/2)
    else:
        mid = int(d/2)+1
        
    length = len(expenditure)

    current = 0
    while end<length:
        median = getMedian(countExp,d,mid)
        if expenditure[end]>=2*median:
            notif+=1
        countExp[expenditure[current]]-=1
        countExp[expenditure[end]]+=1
        current+=1
        end+=1
    
    return notif
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
