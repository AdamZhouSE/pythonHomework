ori=input()
nums=[]
k=int(input())
for i in range(1,len(ori)-1):
    if ori[i]!=',':
        nums.append(int(ori[i]))
nums.sort()
result=[]
for i in range(len(nums)):
    n=i+1
    while n<len(nums):
        result.append(nums[n]-nums[i])
        n += 1
result.sort()
if len(result)>0:
    print(result[k-1])
else:
    print(0)