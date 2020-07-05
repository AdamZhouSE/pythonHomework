nums = eval(input())
low = int(input())
hig = int(input())
res = 0
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if sum(nums[i:j+1])<=hig and sum(nums[i:j+1])>=low:
            res+=1
print(res)