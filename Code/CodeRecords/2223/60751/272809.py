nums=input().split(",")
nums_=[]
for i in nums:
    nums_.append(int(i))
nums_.sort()
l=[]
for i in range(len(nums_)):
    if nums_[i]!=i+1:
        if nums_[i]==nums_[i-1]:
            l.append(nums_[i-1])
        l.append(nums_[i])
if l[0]==l[1]:
    print([l[0],l[-1]+1])
else:
    print([l[-1],l[0]-1])