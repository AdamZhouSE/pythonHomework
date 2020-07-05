nums=input().split(",")
max=-1000000
sum=0
for i in nums:
    sum+=int(i)
    if sum>max:
        max=sum
    if sum<0:
        sum=0
print(max)