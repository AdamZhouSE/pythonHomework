n =int(input())
nums=[]
num =[]
for i in range(0,n):
    nums.append(input().split(','))
    for j in range(0,n):
        num.append(int(nums[i][j]))
k =int(input())

for i in range(0,k-1):
    del num[num.index(min(num))]
print(min(num))