def shuzu(a,lower,upper):
    sums=[]
    for i in range(1,len(a)+1):
        nums=0
        for j in range(0,i):
            nums=a[j]+nums
        sums.append(nums)
    res=0
    for i in range(0,len(sums)):
        for j in range(i,len(sums)):
            if sums[j]>=sums[i]+lower  and sums[j]<=sums[i]+upper:
                res=res+1
    return res
a=eval(input())
lower=int(input())
upper=int(input())
print(shuzu(a,lower,upper))