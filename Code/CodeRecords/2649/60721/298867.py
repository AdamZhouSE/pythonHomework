T=int(input())
for i in range(0,T):
    n,l,r=map(int,input().split(" "))
    s=[]
    while(n>0):
        a=n%2
        n=int(n/2)
        s.append(a)
    s.reverse()
    for i in range(len(s)-r,len(s)-l+1):
        if(s[i]==0):
            s[i]=1
        else:s[i]=0
    re=0
    for i in range(0,len(s)):
        re+=s[i]*int(pow(2,len(s)-1-i))
    print(re)