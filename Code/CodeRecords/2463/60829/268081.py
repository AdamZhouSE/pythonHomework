def find(list,a):
    judge=1
    res=[]
    for i in range(0,len(list)):
        for j in range(0,len(list)):
            if not i==j and list[i]+list[j]==a:
                judge=0
                if i<j:
                    res.append(i+1)
                    res.append(j+1)
                else:
                    res.append(j+1)
                    res.append(i+1)
    if judge==1:
        return None
    else:
        return res[0:2]
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