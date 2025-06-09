m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))

set1_diff = set1.difference(set2)
set2_diff = set2.difference(set1)

ans = []

for i in set1_diff:
    ans.append(i)
    
for i in set2_diff:
    ans.append(i)
    
ans.sort()
for i in ans:
    print(i)