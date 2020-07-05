s1='['+input()+']'
startTime=eval(s1)
s2='['+input()+']'
endTime=eval(s2)
s3='['+input()+']'
profit=eval(s3)
def sche(startTime,endTime,profit):
    n=len(startTime)
    #按照结束时间排序
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
print(sche(startTime,endTime,profit))