t=int(input())
for _ in range(t):
    n=int(input())
    nums=input().split(' ')
    nums=[int(x) for x in nums]
    res=[]
    for i in range(n):
        mul=1
        for j in range(n):
            if j!=i:
                mul*=nums[j]
        res.append(mul)
    res=[str(x) for x in res]
    print(' '.join(res)+' ')