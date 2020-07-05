t=int(input())
for i in range(0,t):
    n=int(input())
    counter=1
    while(True):
        if counter**2<n:
            counter+=1
        else:
            break
    if(counter**2==n):
        print(1)
    else:
        print(0)