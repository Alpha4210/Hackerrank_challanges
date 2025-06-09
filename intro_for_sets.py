

def average(array):
    s1 = set()
    for i in array:
        s1.add(i)
    sum = 0
    for i in s1:
       sum = sum+i
    avg = round(sum/len(s1),3)
    return avg 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)