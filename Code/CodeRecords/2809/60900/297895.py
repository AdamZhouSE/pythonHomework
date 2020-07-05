n = int(input())
nums = input().split(' ')
for i in range(0,n):
    nums[i] = int(nums[i])
temp =[]
for i in range(0,n):
    temp.append(nums[i])
big =0
bigs = 0
if n%2==0:
    bigs = int(n/2)
else:
    bigs = int((n+1)/2)
for i in range(0,bigs):
    big+=max(nums)
    del nums[nums.index(max(nums))]
small = 0
for i in range(0,len(nums)):
    small +=nums[i]
result = small*small+big*big


print(result)
