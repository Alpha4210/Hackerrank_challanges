def swap_case(s):
    x = ""
    for i in s:
        if i.isupper():
            x = x+i.lower()
        elif i.isdigit():
            x = x + i
        elif i.islower:
            x = x+i.upper()
        else:
            x = x+i
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)