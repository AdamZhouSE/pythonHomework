

inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i]=int(nums[i])
res = 0


for i in range(inp+1):
    op = True
    for j in range(inp-1):
        if(nums[j]>nums[j+1]):
            op = False
            break
    re = nums[0]
    nums[0]=nums[inp-1]
    nums[inp-1]=re
    if(op==True):
        break
    res+=1
    if (op == False and i == inp):
        res = -1

print(res)
    