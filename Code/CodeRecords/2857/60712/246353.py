n = int(input())
nums = list(map(int,input().split()))
result = 0
nums.sort()
for i in range(nums[0]):
    bl = True
    for j in range(n):
        if nums[j]%nums[i]!=0:
            bl = False
            break
    if bl:
        result=result+1
print(result)