import math

res=[]
def judgeSquare(num):
    return int(math.sqrt(num))**2==num

def cal(before,nums):
    i=0
    while i<len(nums):
        temp=before.copy()
        temp.append(nums[i])
        if judgeSquare(nums[i]+temp[-2]):
            if len(nums)==1 and temp not in res:
                res.append(temp)
                break
            cal(temp,nums[0:i]+nums[i+1:])
        i+=1

nums=list(map(int,input().split(",")))
i=0
while i<len(nums):
    before=list()
    before.append(nums[i])
    cal(before,nums[0:i]+nums[i+1:])
    i+=1
print(len(res))