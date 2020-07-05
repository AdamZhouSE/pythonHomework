def a(s):
    res=[]
    for i in range(0,len(s)):
        res.append(s[i])
    return res
def change(s,i,j):
    res=""
    for k in range(0,len(s)):
        if k==i:
            res=res+s[j]
        elif k==j:
            res=res+s[i]
        else:
            res=res+s[k]
    return res
def dele(x):
    z=""
    for i in range(0,len(x)):
        if  not x[i]==" " and not x[i]=="." and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
s=str(input())
n=[int(x) for x in dele(str(input())).split(",")]
nn=[]
for i in n:
    if not i in nn:
        nn.append(i)
re=[]
nn.sort()
for i in nn:
    re.append(s[i])
re.sort()
res=""
count=0
for i in range(0,len(s)):
    if not i in nn:
        res=res+s[i]
    else:
        res=res+re[count]
        count=count+1
print(res)