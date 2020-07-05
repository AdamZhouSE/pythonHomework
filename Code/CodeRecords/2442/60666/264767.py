nums=eval(input())
if len(nums)<2:
    print(0)
else:
    nums.sort()
    lst=[]
    for i in range(len(nums)-1):
        lst.append(nums[i+1]-nums[i])
    lst.sort()
    print(lst[-1])