nums=input().split(",")
nums_=[]
for i in nums:
    nums_.append(int(i))
nums_.sort()
a=0
for i in range(1,len(nums_)):
    a+=nums_[i]-nums_[0]
print(a)
