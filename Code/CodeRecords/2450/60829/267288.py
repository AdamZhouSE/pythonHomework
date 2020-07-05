def find(list,a):
    judge=1
    x=[]
    for i in range(0,len(list)):
        if list[i]==a:
            judge=0
            x.append(i)
    if judge==1:
        return [-1,-1]
    else:
        return [x[0],x[len(x)-1]]
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")":
            z=z+x[i]
    return z
aa=str(input())
b=int(input())
a=[int(x) for x in dele(aa).split(",")]
x=find(a,b)
print(x)