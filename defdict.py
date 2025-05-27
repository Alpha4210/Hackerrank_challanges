from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)
for i in range(n):
    x = input()
    a[x].append(i+1)
        
for i in range(m):
    x = input()
    if x in a.keys():
        print(*a[x]) #used to print the elements of a list
    else:
        print(-1)