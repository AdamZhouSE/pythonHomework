nums=list(map(int,input()[1:-1].split(",")))
length=nums.__len__()
i=1
Duan=1
while i<len(nums):
    if max(nums[:i])>min(nums[i:]):
        i=i+1
    else:
        nums=nums[i:]
        Duan=Duan+1
        i=1
print(Duan)