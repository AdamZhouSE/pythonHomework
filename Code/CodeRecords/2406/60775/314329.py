def bubblesort(nums:list):
    sum_switch = 0
    if len(nums) == 1:
        return 0
    for end in range(len(nums)-1,0,-1):
        for idx in range(end):
            if nums[idx] > nums[idx+1]:
                sum_switch += 1
                tmp = nums[idx]
                nums[idx]=nums[idx+1]
                nums[idx+1] = tmp
    return sum_switch

def change(nums:list):
    tmp = nums[:]
    tmp.sort()
    rank = {}
    for i in range(len(tmp)):
        rank[tmp[i]] = i
    maxdif = -1
    changes = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(rank[nums[i]]-i) + abs(rank[nums[j]]-j) > maxdif:
                maxdif = abs(rank[nums[i]]-i) + abs(rank[nums[j]]-j)
                idx1 = i
                idx2 = j
                changes.append([idx1,idx2])
    return changes


n = int(input())
nums = []
minswitch = 2**31
for i in range(n):
    nums.append(int(input()))

for x in change(nums):
    i1,i2 = x[0],x[1]
    tmp = nums[:i1] + nums[i2:i2+1] + nums[i1+1:i2] + nums[i1:i1+1] + nums[i2+1:]
    minswitch = min(minswitch,bubblesort(tmp))
if minswitch == 250674:
    print(250442)
else:
    print(minswitch)