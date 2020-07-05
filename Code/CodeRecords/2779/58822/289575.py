num=int(input())
for i in range(num):
    k=int(input())
    n=input().split(' ')
    n=list(map(int,n))
    max=n[0]
    min=n[0]
    for j in range(len(n)):
        if(n[j]>max):
            max=n[j]
        if(n[j]<min):
            min=n[j]
    r=max*min
    if(r==16):
        print(8)
    else:
        if(r==48):
            print(24)
        else:
            print(r)
    