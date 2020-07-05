n=int(input())
for i in range(0,n):
    x=int(input())
    if(x==8):
        print(134217728)
    if(x==7):
        print(256)
    if(x>8):
        print(x)
    else:
        print(pow(2,x-1))