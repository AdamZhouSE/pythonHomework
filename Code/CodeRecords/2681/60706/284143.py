t=int(input())
for i in range(t):
    n=int(input())
    count=0
    while(n!=0):
        if n%2==0:
            n=int(n/2)
            count=count+1
        else:
            n=n-1
            count=count+1
    print(count)