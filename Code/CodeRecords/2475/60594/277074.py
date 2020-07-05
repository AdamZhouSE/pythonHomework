def maxNum(num,i,maxn,muqian):
    if i==len(num):
        print(max(maxn,muqian))
        return
    if num[i] - num[i - 1] > 1:
        maxn = max(muqian, maxn)
        maxNum(num,i+1,maxn,1)
    else:
        maxNum(num,i+1,maxn,muqian+1)
n=(int)(input())
for i in range(n):
    a=int(input())
    num=[int(n) for n in input().split()]
    num.sort()
    oc=[]
    for i in num:
        cunzai=False
        for j in oc:
            if i==j:
                cunzai=True
                break
        if not cunzai:
            oc.append(i)
    num=oc
    maxNum(num,1,0,1)