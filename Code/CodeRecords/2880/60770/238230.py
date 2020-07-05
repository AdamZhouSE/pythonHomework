def solve():
    weight=int(input().split()[1])
    nums = list(map(int, input().split()))
    away=[0 for i in range(len(nums))]
    res=0
    for i in range(len(nums)):
        if nums[i]>weight:
            break
        if away[i]==0:
            away[i]=1
            res+=1
    nums.reverse()
    away.reverse()
    for i in range(len(nums)):
        if nums[i]>weight:
            break
        if away[i]==0:
            away[i]=1
            res+=1
    print(res)


if  __name__ == '__main__' :
    solve()