input()
nums=[int(x) for x in input().split()]
count=0
for i in range(1,min(nums)):
    judge=True
    for j in nums:
        if j%i!=0:
            judge=False
            break
    if judge:
        count+=1
print(count)