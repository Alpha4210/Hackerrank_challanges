# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())

a = input().split()

k = int(input())

result = list(combinations(a, k))
# print(result)

count = 0

for i in result:
    if 'a' in i:
        count+=1

print(count/len(result))