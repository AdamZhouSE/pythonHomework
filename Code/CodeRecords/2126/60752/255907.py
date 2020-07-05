nums=list(map(int,input().split(',')))
lst=[]
max=[]
for i in range(len(nums)):
    lst = []
    lst.append(nums[i])
    if i<len(nums)-1:
        for j in nums[i+1:]:
            if j%lst[len(lst)-1]==0:
                lst.append(j)
    if len(lst)>len(max):
        max=lst
print(max)