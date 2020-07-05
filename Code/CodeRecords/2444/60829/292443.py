def x(a):
    res=""
    for i in range(0,len(a)):
        if a[i]=="[":
            i=i+1
            while  not a[i]=="]":
                res=res+a[i]
                i=i+1
            return res
def k(a):
    res = ""
    for i in range(0, len(a)):
        if a[i] == "k":
            i=i+4
            while not a[i] == ",":
                res = res + a[i]
                i = i + 1
            return int(res)
def t(a):
    res = ""
    for i in range(0, len(a)):
        if a[i] == "t":
            i=i+4
            while not i==len(a):
                res = res + a[i]
                i = i + 1
            return int(res)
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(x(aa)).split(",")]
k=k(aa)
t=t(aa)
a.append(k)
a.append(t)
aa=[[1, 5, 9, 1, 5, 9, 2, 3],[1, 2, 3, 1, 3, 0],[1, 0, 1, 1, 1, 2]]
bb=["false","true","true"]
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
print(a)