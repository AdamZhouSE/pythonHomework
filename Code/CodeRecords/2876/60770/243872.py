def solve():
    input()
    nums = list(map(int, input().split()))
    res=0
    for i in range(1,len(nums)-1):
        if nums[i-1]==1 and nums[i+1]==1 and nums[i]==0:
            nums[i+1]=0
            res+=1
    print(res)

if  __name__ == '__main__' :
    solve()