n = int(input())
nums = [int(i) for i in input().split(" ")]
odd = []
even = []
for i in range(n):
    if nums[i]%2 ==1:
        odd.append(nums[i])
    else:
        even.append(nums[i])
even.sort()
odd.sort()
sum = 0
if len(even) == len(odd) or len(even)-len(odd) == 1  or len(even)-len(odd)==-1:
    print(0)
elif(len(even)>len(odd)):
    for i in range(0,len(even)-len(odd)-1):
        sum+=even[i]
    print(sum)
else:
    for i in range(0,len(odd)-len(even)-1):
        sum+=odd[i]
    print(sum)
