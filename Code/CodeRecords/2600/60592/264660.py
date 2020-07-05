tests = int(input())
nums = list(map(int,input().split()))
comd = list(map(int,input().split()))
for i in range(0,tests):
    lc = comd[i]-1
    nums[lc] = -1
    j = 0
    res = 0
    sums = 0
    while j < len(nums):
        if nums[j]==-1:
            if sums>res:
                res=sums
            sums=0
            j+=1
            continue
        sums+=nums[j]
        j+=1
    if res < sums:
        res = sums
    print(res)