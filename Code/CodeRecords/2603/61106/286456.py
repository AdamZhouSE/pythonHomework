ori=input()
nums=ori.split(",")
nums=nums[1:len(nums)-1]
k=int(input())
if nums[-1]==']':
    print(0)
else:
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    nums.sort()
    result=[]
    for i in range(len(nums)):
        n=i+1
        while n<len(nums):
            result.append(nums[n]-nums[i])
            n += 1
    result.sort()
    print(result[k-1])