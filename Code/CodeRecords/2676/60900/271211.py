n = int(input())
command = []
nums = []
for i in range(0,n):
    command.append(int(input().split(' ')[1]))
    nums.append(input().split(' '))

for i in range(0,n):
    for j in range(0,len(nums[i])):
        nums[i][j] = int(nums[i][j])

for i in range(0,n):
    count = 0
    for j in range(0,len(nums[i])-command[i]+1):
        temp = 0
        for m in range(j,j+command[i]):
            temp = temp+nums[i][m]
        if temp>count:
            count = temp
        j = j+1
    print(count)
