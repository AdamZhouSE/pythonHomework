n=int(input())
for i in range(n):
    l=input()
    dp=[1 for _ in range(len(l))]
    t=len(l)
    m=set()
    d=0
    r=1
    while(t>0):
        for j in range(t):
            dp[j]=dp[j]*int(l[j+d])
            if dp[j] in m:
                r=0
                break
            m.add(dp[j])
        t-=1
        d+=1
    print(r)

