# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k, m = list(map(int, input().split()))
n=[]
for i in range(k):
    a = list(map(int, input().split()))
    b = a[1:]
    n.append(b)
    
result = list(product(*n))
r=[]
for i in result:
    sum = 0
    for j in i:
        sum += j**2
    r.append(sum%m)

print(max(r))