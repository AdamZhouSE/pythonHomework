t = int(input())
for i in range(0,t):
    n = int(input())
    if(n % 2 == 1):
        print(int(pow(2,pow(2,(n - 1) / 2))))
    else:
        print(int(pow(2,pow(3,(n - 2) / 2))))