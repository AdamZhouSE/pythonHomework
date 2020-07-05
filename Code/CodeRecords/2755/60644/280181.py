t=int(input())
for i in range(0,t):
    a=input().split()
    s1=input().split()
    s2=input().split()
    m=max(int(a[0]),int(a[1]))
    while len(s1)<2*m:
        s1=s1+[0]
    while len(s2)<2*m:
        s2=s2+[0]
    res=[0]*(2*m-1)
    for j in range(0,len(res)):
        for k in range(0,j+1):
            res[j]=res[j]+int(s1[k])*int(s2[j-k])
    for j in range(len(res)-1,0,-1):
        if res[j]==0:
            del res[j]
        else:
            break
    for j in range(0,len(res)):
        res[j]=str(res[j])
    print(' '.join(res))
