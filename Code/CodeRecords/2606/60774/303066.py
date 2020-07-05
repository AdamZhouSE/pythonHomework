nums = list(map(int,input()[1:-1].split(',')))
target = int(input())
if(target in nums):
    print(nums.index(target))
else:
    print(-1)