def find(list):
    z=list[0]
    for i in range(0,len(list)):
        if z>list[i]:
            z=list[i]
    return z
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