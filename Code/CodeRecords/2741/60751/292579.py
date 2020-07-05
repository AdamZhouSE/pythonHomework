nums=list(map(int,input().strip('[').strip(']').split(",")))
len_=1
max_=0
l=[]
for i in range(len(nums)):
    if i!=len(nums)-1 and nums[i]<nums[i+1]:
        len_+=1
        l.append(nums[i])
    else:
        if len_>max_:
            max_=len_
        l=[]
        len_=1
print(max_)