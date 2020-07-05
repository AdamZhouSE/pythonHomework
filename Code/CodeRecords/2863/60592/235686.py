nums = input().split(' ')
base = int(nums[0])
wall = int(nums[1])
kid = input().split(' ')
kid.sort()
for i in range(0,len(kid)):
    if int(kid[i]) > wall:
        base+=len(kid)-1-i
        break
print(base)