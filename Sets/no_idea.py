n, m = list(map(int, input().split()))
l1 = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

hapiness = 0
for i in l1:
    if(i in a):
        hapiness+=1
    elif(i in b):
        hapiness-=1
    else:
        continue

print(hapiness)