num=int(input())
def judge(num):
    res=[]
    for x in range(1, num):
        if num%x==0:
            res.append(x)
    sum=0
    for h in res:
        sum+=h
    if sum==num:
        return True
    else:
        return False