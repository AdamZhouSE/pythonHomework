n = int(input())
nums = []
for i in range(0,n):
    nums.append(input().split(','))
    for j in range(0,n):
        nums[i][j] = int(nums[i][j])
result = 0
for i in range(0,n):
    for j in range(0,n):
        if nums[i][j]!=0:
            result+=2
        if nums[i][j]==0:continue
        for m in range(1,nums[i][j]+1):
            max =4
            if i!=0 and nums[i-1][j]>=m:
                max-=1
            if j!=0 and nums[i][j-1]>=m:
                max-=1
            if i!=n-1 and nums[i+1][j]>=m:
                max-=1
            if j!=n-1 and nums[i][j+1]>=m:
                max-=1
            result+=max
print(result)