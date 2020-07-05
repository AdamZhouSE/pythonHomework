nums=input().split(",")
nums_=[]
sum=0
for i in nums:
    nums_.append(int(i))
    sum+=int(i)
k=0
m=0
average=sum/len(nums)
average1=int(str(average).split(".")[0])
average2=average1+1
for i in range(len(nums_)):
    k+=abs(nums_[i]-average1)
for i in range(len(nums_)):
    m+=abs(nums_[i]-average2)
print(min(m,k))
