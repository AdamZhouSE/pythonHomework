def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
a=str(input())
aa=[int(x) for x in dele(a).split(",")]
x=0
aa.sort()
for i in range(0,len(aa)-1):
    if aa[i+1]-aa[i]>x:
        x=aa[i+1]-aa[i]
print(x)