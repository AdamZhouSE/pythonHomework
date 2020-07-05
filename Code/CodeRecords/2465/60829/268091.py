def find(a):
    h=1
    for i in range(1,len(a)):
        if a[len(a)-1-i]>=h+1:
            h=h+1
    return h
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
x=find(a)
print(x)