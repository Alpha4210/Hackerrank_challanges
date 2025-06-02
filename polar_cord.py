import cmath as cm

num = input()

if(complex(num)):
    print(abs(complex(num)))
    print(cm.phase(complex(num)))