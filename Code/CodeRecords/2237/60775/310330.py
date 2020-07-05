inpu2 = input().split(' ')
n = int(inpu2[0])
m = int(inpu2[1])

nums = [x for x in range(1,n+1)]
for i in range(m):
    opt = [int(x) for x in input().split(' ')]
    nums[opt[0]-1 : opt[1]] = reversed(nums[opt[0]-1 : opt[1]])

print(' '.join(str(x) for x in nums),end=' ')
