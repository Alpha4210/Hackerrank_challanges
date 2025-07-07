# importing math module
import math

#Taking input from user and assinging it to m and n.
n,m = map(int, input().split())

# Variables having number of rows in upper and lower part (respective to welcome)
u_part = math.floor(n/2)
l_part = math.floor(n/2)

# Code for upper part (respective to welcome)
char = ".|."
width = m
for i in range(1, u_part+1):
    print((char*((2*i)-1)).center(width, "-"))

# Code for welcome
wel = "WELCOME"
print(wel.center(width, "-"))

# Code for lower part(respective to welcome)
for i in range(l_part, 0, -1):
    print((char*((2*i)-1)).center(width, "-"))
