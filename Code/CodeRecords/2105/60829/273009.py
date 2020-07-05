def k(x):
    if x<0:
        x=-1*x
    return x
def max(x,y):
    if x>=y:
        return x
    else:
        return y
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
x=k(int(int(a[0])-int(a[2])))*k(int(int(a[1])-int(a[3])))
y=k(int(int(a[4])-int(a[6])))*k(int(int(a[5])-int(a[7])))
print(x+y-6)