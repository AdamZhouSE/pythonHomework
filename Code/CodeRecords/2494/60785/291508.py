nums=[int(i) for i in input().strip('[|]').split(',')]
n=len(nums)
count=0
for i in range(n):
    for j in range(i,n):
        if nums[i] > 2*nums[j]:
            count+=1
print(count)