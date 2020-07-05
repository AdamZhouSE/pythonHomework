nums = eval(input())
counts = []
cnt = 0
for i in range(0,len(nums)):
    for j in range (i,len(nums)):
        if nums[i]>nums[j]:
            cnt+=1
    counts.append(cnt)
    cnt = 0
print(counts)