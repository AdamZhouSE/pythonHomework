nums = eval(input())
lower = int(input())
upper = int(input())
res = 0
n = len(nums)
for i in range(n):
    for j in range(i+1,n+1):#n+1很关键
        temp = 0
        for k in range(i,j):
            temp+=nums[k]
        if(temp<=upper and temp>=lower):
            res+=1
print(res)