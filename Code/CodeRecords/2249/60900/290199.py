n =int(input())
nums =[]
nums2 =[]
for i in range(0,n):
    a = input().split(',')
    nums.append(a)

for i in range(0,n):
    for j in range(0,n):
        b = int(nums[i][j])
        nums[i][j]=b
count =0
for i in range(0,n):
    big =0
    for j in range(0,n):
        if nums[i][j]!=0:
            count+=1
        big=max(big,nums[j][i])

    count+=max(nums[i])
    count+=big

print(count)
