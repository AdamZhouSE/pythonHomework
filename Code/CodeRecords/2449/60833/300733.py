nums=list(map(int,input().split(',')))
t=int(input())
if t not in nums:
    print(-1)
else:
    print(nums.index(t))
