# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))

N = int(input())
for i in range(N):
    x = input().split()
    y = set(map(int, input().split()))
    if(x[0]=='update'):
      a.update(y)  
    elif(x[0]=='intersection_update'):
        a.intersection_update(y)
    elif(x[0]=='difference_update'):
        a.difference_update(y)
    elif(x[0]=='symmetric_difference_update'):
        a.symmetric_difference_update(y)

sum = 0
for i in a:
    sum+=i
print(sum)