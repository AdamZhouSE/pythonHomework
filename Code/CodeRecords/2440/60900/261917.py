n = input()

nums = n[1:-1].split(",")

for i in range (0,len(nums)):
    nums[i] = int(nums[i])

print("[",end='')
print(min(nums),end='')
del nums[nums.index(min(nums))]

while len(nums)!=0:
    print(", ",end='')
    print(min(nums),end='')
    del nums[nums.index(min(nums))]

print("]")

    