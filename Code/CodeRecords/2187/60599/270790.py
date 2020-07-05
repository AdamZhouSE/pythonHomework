u=int(input())
for p in range(u):
    maxS=0
    tmp=0
    s=list(map(int,input().split(' ')))
    nums = list(map(int, input().split(' ')))
    for i in range(0,len(nums)):
        if(i+s[1]>len(nums)):
            break
        for k in range(s[1]):
            tmp+=nums[i+k]
        maxS=max(maxS,tmp)
        tmp=0
    print(maxS)
