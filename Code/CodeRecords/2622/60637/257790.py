array=eval(input())
nums=[]
frequency=[]
for num in array:
    if(num not in nums):
        nums.append(num)
        frequency.append(1)
    else:
       frequency[nums.index(num)]+=1
for i in range(0,len(nums)):
    if(frequency[i]>len(array)/2):
        print(nums[i])