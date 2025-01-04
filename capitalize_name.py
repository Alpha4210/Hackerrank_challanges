

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    
    name = s.split() # To split the name in a list
    print(name)
    
    x = [] #New list where the capitalized name will be stored
    
    # Code to capitalize the name and insert in the new list
    for i in name:
        a = i.capitalize()
        x.append(a)
    
    # Giving the result
    l = ""
    for i in x:
        l = l + i + ' '
    return l

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
