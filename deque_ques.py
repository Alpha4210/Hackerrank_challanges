from collections import deque
d=deque()
n=int(input())

for i in range(n):
    ask=input()
    a=ask.split()    
    if a[0]=="append":
        d.append(a[1])
    elif a[0]=="pop":   
        d.pop()
    elif a[0]=="popleft":
        d.popleft()
    elif a[0]=="appendleft":
        d.appendleft(a[1])
    else:
        print("Give a valid input")
        
for i in d:
    print(i, end=" ")