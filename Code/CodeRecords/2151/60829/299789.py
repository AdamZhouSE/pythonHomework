def tran(x):
    res=""
    while x>0:
        t=str(x%3)
        res=t+res
        x=(x-x%3)//3
    if len(res)<16:
        for i in range(16-len(res)):
            res="0"+res
    return res
def add(x,y):
    res=""
    for i in range(16):
        k=int(x[i])
        kk=int(y[i])
        res=res+str((kk+k)%3)
    return  res
n,o=[int(x) for x in input().split(" ")]
count=tran(0)
for p in range(o):
    a,b,c=[int(x) for x in input().split(" ")]
    count=add(count,tran(c))
print(int(count,3))