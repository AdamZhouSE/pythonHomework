def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" ":
            z=z+x[i]
    return z
a=str(input()).split(",")
aa=[x for x in dele(a[0])[1:len(a[0])-1]]
bb=[x for x in dele(a[1])[1:len(a[1])-1]]
aa.sort()
bb.sort()
if aa==bb:
    print("true")
elif not aa==bb:
    print("false")