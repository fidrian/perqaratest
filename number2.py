#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # no obstacles
    left = c_q-1
    right = n-c_q
    up = n-r_q
    down = r_q-1    
    upleft = left if left<up else up
    upright = right if right<up else up
    downleft = left if left<down else down
    downright = right if right<down else down
    
    #presented obstacles
    for obs in obstacles:
        row = obs[0]
        col = obs[1]
        
        if row==r_q and col<c_q:
            if c_q-col-1<left:
                left = c_q-col-1
                
        elif row==r_q and col>c_q:
            if col-c_q-1<right:
                right = col-c_q-1
                
        elif row>r_q and col==c_q:
            if row-r_q-1<up:
                up = row-r_q-1
                
        elif row<r_q and col==c_q:
            if r_q-row-1<down:
                down = r_q-row-1
                
        elif row>r_q and col<c_q:
            if row-r_q == c_q-col:
                if row-r_q-1<upleft:
                    upleft = row-r_q-1
                    
        elif row>r_q and col>c_q:
            if row-r_q == col-c_q:
                if row-r_q-1<upright:
                    upright = row-r_q-1
                    
        elif row<r_q and col<c_q:
            if r_q-row == c_q-col:
                if r_q-row-1<downleft:
                    downleft = r_q-row-1
                    
        elif row<r_q and col>c_q:
            if r_q-row == col-c_q:
                if r_q-row-1<downright:
                    downright = r_q-row-1
                    
    attack = left + right + up + down + upleft + upright + downleft + downright
    return attack

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
