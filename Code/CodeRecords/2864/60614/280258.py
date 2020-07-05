length=int(input())
nums=[int(x) for x in input().split()]
count=[]
for i in range(max(nums)+1):
    count.append(nums.count(i))
first=0
second=count[1]
for i in range(2,max(nums)+1):
    temp=second
    second=max(second,first+count[i]*i)
    first=temp
print(second)