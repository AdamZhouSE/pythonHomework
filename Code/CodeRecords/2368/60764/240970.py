T=int(input())
for t in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    res=[]
    for i in range(n):
        if i%2==0:
            res.append(nums.pop(nums.index(max(nums))))
        else:
            res.append(nums.pop(nums.index(min(nums))))
    print(' '.join(str(j) for j in res))