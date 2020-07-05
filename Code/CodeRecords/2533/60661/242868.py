nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
arr1=[];arr2=[]
for i in range(len(nums)):
    if nums[i]%2==0:
        arr1.append(nums[i])
    else:
        arr2.append(nums[i])
arr1.extend(arr2)
print(arr1)