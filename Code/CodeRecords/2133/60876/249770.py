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
def plus():
    index=nums.index(max())
    for i in range(0,len(nums)):
        if i!=index:
            nums[i]+=1
time=0
while not right():
    plus()
    time+=1
print(time)