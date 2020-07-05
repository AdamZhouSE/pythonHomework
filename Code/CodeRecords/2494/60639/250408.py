inp=input().strip('[').strip(']').split(',')
nums=[]
for i in range(len(inp)):
    nums.append(int(inp[i]))
count=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]>2*nums[j]:
            count+=1
        else:
            continue
print(count)