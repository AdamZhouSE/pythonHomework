nums=input()
lower=int(input())
upper=int(input())
count=0
for x in range(0,len(nums)):
    temp=0
    for j in range(x, len(nums)):
        temp+=nums[j]
        if temp >= lower and temp<= upper:
            count+=1
print(count) 