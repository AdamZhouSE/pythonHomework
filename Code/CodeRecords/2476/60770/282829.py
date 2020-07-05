def solve():
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    res=0
    while len(nums)>1:
        nums[1]+=nums[0]
        res+=nums[1]
        del nums[0]
        nums.sort()
    print(res)

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()