def print_formatted(n):
    for i in range(1, n+1):
        print(i)
        print(oct(i).replace("0b", ""))
        print(hex(i).replace("0b", ""))
        print(bin(i).replace("0b", ""))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
