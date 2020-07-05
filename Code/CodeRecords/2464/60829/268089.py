def find(list,a):
    judge=1
    res=6
    if sum(list)<a:
        res=0
    else:
        count=6
        for i in range(0,len(list)):
            for j in range(i+1,len(list)):
                if sum(list[i:j+1])>a:
                    count=j-i
                    if count<res:
                        res=count
    return res
def sum(a):
    x=0
    for i in range(0,len(a)):
        x=x+a[i]
    return x
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")":
            z=z+x[i]
    return z
b=int(input())
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
x=find(a,b)
print(x)