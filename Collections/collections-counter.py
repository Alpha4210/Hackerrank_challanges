from collections import Counter
x = int(input())
y = Counter(map(int, input().split()))
z = int(input())

total = 0
for i in range(z):
    a,b = list(map(int, input().split()))
    if(y[a]>0):
        total+=b
        y[a]-=1

print(total)