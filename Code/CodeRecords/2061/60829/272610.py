def c(x):
    c=""
    for i in range(0,len(x)):
        if x[i]=="{":
            i=i+1
            while not x[i]=="}":
                c=c+x[i]
                i=i+1
            return c
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
a=str(input())
aa=[int(x) for x in dele(c(a)).split(",")]
c=0
for i in range(1,len(aa)):
    if aa[i]==aa[0]:
        c=i
print(len(aa)+1-c)