n=int(input())
res=[]
for i in range(n):
    num=int(input())
    this=0
    if num==1: this=2
    elif num==2: this=3
    else:
        list=[2,3]
        while len(list)<num:
            list.append(list[-1]+list[-2])
        this=list[-1]
    res.append(this)
for e in res:print(e)