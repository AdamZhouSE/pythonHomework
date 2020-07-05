n = int(input())
nums = list(input())
count = 0
for i in range(n-1):
    if nums[i] == nums[i+1]:
        count+=1
print(count)        
