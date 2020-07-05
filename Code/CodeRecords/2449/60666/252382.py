nums=list(map(int,input().strip().split(",")))
target=int(input())
if target not in nums:
    print(-1)
else:
    print(nums.index(target))