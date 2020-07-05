def solve():
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    res=0
    for num in nums:
        res+=n*num
        n-=1
    res-=nums[0]
    print(res)
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()