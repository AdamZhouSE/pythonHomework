def find(list,a):
    judge=1
    for i in range(0,len(a)):
        for
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