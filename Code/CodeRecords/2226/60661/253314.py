def judge(num):
    if str(num).__contains__('0'):
        return False
    for i in range(len(str(num))):
        if num%int(str(num)[i])!=0:
            return False
    return True

left=int(input())
right=int(input())
res=[]
for i in range(left,right+1):
    if judge(i):
        res.append(i)
print(res)