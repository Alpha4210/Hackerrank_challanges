# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()
result = [(len(list(group)), n) for n, group in groupby(s)]

for i in result:
    i = list(i)
    i[1] = int(i[1])
    i = tuple(i)
    print(i, end=' ')