def cc(a):
    for i in range(0,len(a)):
        count=0
        for j in range(0,len(a)):
            if a[j]==a[i]:
                count=count+1
        if count>len(a)//2:
            return a[i]
    return -1
def dele(x):
    z=""
    for i in range(0,len(x)):
        if  not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
n=int(input())
x=[]
for i in range(0,n):
    num=int(input())
    aa=str(input())
    a=[int(x) for x in dele(aa).split(" ")]
    x.append(a)
res=[]
for i in range(0,n):
    res.append(cc(x[i]))
for i in range(0,n):
    print(res[i])
