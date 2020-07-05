N,M=map(int,input().split())
a=list(map(int,input().split()))
for i in range(M):
    s=list(map(int,input().split()))
    if s[0]==1:
        for j in range(s[1]-1,s[2]):
            a[j]+=s[3];
    elif s[0]==2:
        sum=0
        for j in range(s[1]-1,s[2]):
            sum+=a[j]
        print("{:.4f}".format(sum/(s[2]-s[1]+1)))
    else :
        sum1,sum2=0,0
        for j in range(s[1]-1,s[2]):
            sum1+=a[j]
            sum2+=a[j]*a[j]
        n=s[2]-s[1]+1
        print("{:.4f}".format(sum2/n-(sum1/n)*(sum1/n)))