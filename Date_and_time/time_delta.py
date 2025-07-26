#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    delta_time_t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    delta_time_t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    
    difference_delta_time = delta_time_t1 - delta_time_t2
    
    #print(delta_time_t1)
    #print(delta_time_t2)
    #print(int(difference_delta_time.total_seconds()))
    
    output = str(int(difference_delta_time.total_seconds()))
    
    #print(output[0])    
    
    output = output[1:] if output.startswith('-') else output

    return output
    
    return 500
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
