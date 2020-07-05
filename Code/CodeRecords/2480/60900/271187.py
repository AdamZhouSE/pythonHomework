n = int(input())
nums =[]
for i in range(0,n):
    a = int(input())
    temp =input().split(' ')
    for j in range(0,len(temp)):
        temp[j]=int(temp[j])
    nums.append(temp)

for i in range(0,n):
    b = []
    for j in range(0,len(nums[i])):
        if nums[i][j]%2==1:
            b.append(j)
    for j in range(0,len(b)):
        nums[i].append(nums[i][b[j]-j])
        del nums[i][b[j]-j]
    for j in range(0,len(nums[i])):
        print(nums[i][j],end=' ')
    print("")