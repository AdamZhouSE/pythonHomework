def find(x):
    c=10000
    for i in range(len(x)):
        if x[i]<=c:
            c=x[i]
    return c
def dele(x):
    z=""
    for i in range(0,len(x)):
        if  not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
n=str(input()).split(" ")
x=[]
cc=input()
for i in range(0,int(n[1])):
    aa=str(input())
    a=[int(x) for x in dele(aa).split(" ")]
    x.append(a)
res=[]
for i in range(0,int(n[1])):
    res.append(find(x[i]))
for i in range(0,int(n[1])):
    print(res[i])