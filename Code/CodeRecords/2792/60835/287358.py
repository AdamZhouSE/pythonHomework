n = int(input())
nums = list(map(int,input().split()))
res = []
for n in range(1,len(nums)):
    if nums[n] <= nums[n-1]:
        res.append(nums[n-1])
res.append(nums[-1])
print(len(res))
for x in range(len(res)):
    if x != 0:
        print(' ',end = '')
    print(res[x],end = '')
print()