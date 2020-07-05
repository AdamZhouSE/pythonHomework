nums=list(map(int,input().split(",")))
def right():
    for item in nums:
        if item!=nums[0]:
            return False
    return True
def max():
    max=0
    for item in nums:
        if item>max:
            max=item
    return max
def min():
    min=nums[0]
    for item in nums:
        if item<min:
            min=item
    return min
def middle():
    sum=0
    for item in nums:
        sum+=item
    return sum/len(nums)
time=0
while not right():
    if max()-middle()>middle()-min():
        nums[nums.index(max())]-=1
    else:
        nums[nums.index(min())]+=1
    time+=1
print(time)