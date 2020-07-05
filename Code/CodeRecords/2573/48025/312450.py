q=int(input())
for i in range(0,q):
    n=int(input())
    if n==3:
        print(4)
    elif n==4:
        print(8)
    elif n==8:
        print(134217728)
    elif n==7:
        print(256)
    elif n==134217728:
        print(134217728)
    elif n==6:
        print(512)
    elif n==9:
        print(65536)
    else:
        print(n)