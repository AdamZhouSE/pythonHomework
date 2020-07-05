s1 = input().split(' ')
n =int(s1[0])
p =int(s1[1])
nums = input().split(' ')
for i in range(0,n):
    nums[i] =int(nums[i])
k = int(input())
op =[]
for i in range(0,k):
    op.append(input().split(' '))
    for j in range(0,len(op[i])):
        op[i][j] =int(op[i][j])

for i in range(0,k):
    if op[i][0]==1:
        a =op[i][1]-1
        b =op[i][2]
        for j in range(a,b):
            nums[j] = op[i][3]*nums[j]
    elif op[i][0]==2:
        for j in range(op[i][1]-1,op[i][2]):
            nums[j] = op[i][3]+nums[j]
    else:
        result =0
        for j in range(op[i][1] - 1, op[i][2]):
            result = result + nums[j]
        print(result%p)