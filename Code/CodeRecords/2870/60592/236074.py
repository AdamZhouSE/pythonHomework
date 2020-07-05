odd = []
even = []
num = int(input())
nums = input().split(' ')
for i in range(0,num):
    nums[i] = int(nums[i])
for i in range(0,num):
    if nums[i]%2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
odd.sort()
sum = 0
for i in range(0,len(even)):
    sum+=even[i]
if len(odd)%2==0:
    for i in range(0,len(odd)):
        sum+=odd[i]
else:
    for i in range(0,len(odd)-1):
        sum+=odd[len(odd)-1-i]
print(sum)