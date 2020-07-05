nums=input().split(',')
nums=list(map(int,nums))
target=int(input())
if target not in nums:
    print(-1)
else:
    print(nums.index(target))