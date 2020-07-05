nums=eval(input())
lower=int(input())
upper=int(input())
count=0
for i in range(len(nums)):
    summ=0
    for j in range(i,len(nums)):
        summ+=nums[j]
        if summ>=lower and summ<=upper:
            count+=1
print(count)