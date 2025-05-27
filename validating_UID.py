# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input()) #for getting number of inputs
arr = []
for i in range(n): # for getting the inputs in the array of the input
    x = str(input())
    arr.append(x)

UID_validity = True

letters_list_l_case = "abcdefghijklmnopqrstuvwxyz"
letters_list_u_case = letters_list_l_case.upper()
numbers_list = "1234567890"

u_case = 0
d_count = 0
count = 0
dup_count = 0

for i in arr:
    count +=1
    for j in i:
        if j in letters_list_u_case:
            u_case+=1
        if j in numbers_list:
            d_count+=1
        if i.count(j)>1:
            dup_count+=1
        else:
            continue

if count>10:
    print("Invalid")
elif u_case