t=int(input())
for time in range(0,t):
    n=int(input())
    count=0
    while(n!=0):
        if(n%2==0):
            n=n//2
            count+=1
        else:
            n=n-1
            count+=1
    print(count)