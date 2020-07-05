T=int(input())
for tt in range(T):
    s=input()
    dpa=[0]*len(s)
    dpb=[0]*len(s)
    dpc=[0]*len(s)
    if(s[0]=='a'):
        dpa[0]=1
    for i in range(1,len(s)):
        if(s[i]=='a'):
            dpa[i]=2*dpa[i-1]+1
            dpb[i]=dpb[i-1]
            dpc[i]=dpc[i-1]
        elif(s[i]=='b'):
            dpa[i]=dpa[i-1]
            dpb[i]=dpa[i-1]+dp[i-1]*2
            dpc[i]=dpc[i-1]
        else:
            dpa[i]=dpa[i-1]
            dpb[i]=dpa[i-1]
            dpc[i]=dpb[i-1]+dpc[i-1]*2
    print(dpc[len(s)-1])