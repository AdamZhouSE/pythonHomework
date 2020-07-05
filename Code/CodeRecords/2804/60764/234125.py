str=input()
nums=str.split('+');
nums.sort();
for i in range(len(nums)):
    if i!=len(nums)-1:
        print(nums[i],end="+")
    else:
        print(nums[i])