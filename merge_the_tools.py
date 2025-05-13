def merge_the_tools(string, k):
    a = [string[i:i+k] for i in range(0, len(string), k)]
    i=0;
    while len(a)!=0:
        chr = ''
        for j in a[i]:
            if j in chr:
                continue
            else:
                chr = chr+j      
        print(chr)        
        a.pop(i)        
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)