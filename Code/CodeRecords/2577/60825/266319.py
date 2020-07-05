def jobScheduling(startTime, endTime, profit) -> int:
    n=len(startTime)
    h=sorted(zip(endTime,startTime,endTime,profit))
    w=[0]*n
    for i in range(n-1,-1,-1):
        flag=0
        for j in range(i-1,-1,-1):
            if h[j][2]<=h[i][1]:
                flag=1
                w[i]=j
                break
        if flag==0:
            w[i]=-1
    OPT=[0]*(n+1)
    for i in range(n):
        OPT[i+1]=max(OPT[i],h[i][3]+OPT[w[i]+1])
    return OPT[n]


aaa=input()
l1=aaa.split(",")
l1= list(map(int, l1))
aaa=input()
l2=aaa.split(",")
l2= list(map(int, l2))
aaa=input()
l3=aaa.split(",")
l3= list(map(int, l3))
print(jobScheduling(l1,l2,l3))