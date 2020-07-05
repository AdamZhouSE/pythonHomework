def y(a,b):
    res=[]
    count=1
    cal=0
    car=0
    cbl=0
    cbr=0
    
def ch(x):
    res=""
    for i in range(len(x)):
        if not i==len(x)-1:
            res=res+str(x[i])+" "
        else:
            res=res+str(x[i])
    return res
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    print(ch(res))