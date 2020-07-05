lengths = input().split()
lenA = int(lengths[0])
lenB = int(lengths[1])
nums = input().split()
k = int(nums[0])
m = int(nums[1])
numsA = input().split()
for i in range(0,len(numsA)):
    numsA[i] = int(numsA[i])
numsB = input().split()
for i in range(0, len(numsB)):
    numsB[i] = int(numsB[i])

if numsA[k - 1] >= numsB[lenB - m]:
    print('NO')
else:
    print('YES')