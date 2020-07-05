n = int(input())
nums = []
N=[]
for i in range(0,n):
    nums.append(input().split(" "))
    N.append(int(input()))

for i in range(0,n):
    cha = int(nums[i][1])-int(nums[i][0])
    print(cha*(N[i]-1)+int(nums[i][0]))