def sortcount(start,end,n):
    if(start>end):
        return 0
    if(n==1):
        return(end-start+1)
    else:
        sum=0
        for i in range(start,int(end/2)+1):
            #print(i,end,n-1,sum)
            sum=sum+sortcount(i*2,end,n-1)
            #print(i,sum)
        return sum
t=int(input())
for i in range(t):
    m,n=map(int,input().split(" "))
    ans=sortcount(1,m,n)
    print(ans)