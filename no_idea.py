# Code is correct but exceeding time limit
# n = list(map(int, input().split()))
# n_arr = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# happiness_index = 0

# for i in n_arr:
#     if(i in a):
#         happiness_index+=1
#     if(i in b):
#         happiness_index-=1
        
# print(happiness_index)

# Code with good time complexity
if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    elements_arr = list(map(int, input().strip().split(' ')))
    
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))
    
    for i in elements_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)  