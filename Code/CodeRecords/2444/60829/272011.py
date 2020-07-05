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
judge=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]==t and j-i==k:
            print("true")
            judge=1
        elif a[i]-a[j]==t and j-i==k:
            print("true")
            judge=1
if judge==0:
    print("false")