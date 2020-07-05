# 1+2+3+4+...+n

def check(n):
    nums = list(str(n))
    res = []
    for i in range(len(nums)):
        for j in range(0,len(nums)-i):#从j位开始，往后延伸i位的数字
            sum = 1
            for k in range(j,j+i+1):
                sum *= int(nums[k])
            if sum in res:
                return 0
            res.append(sum)
    return 1








t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
