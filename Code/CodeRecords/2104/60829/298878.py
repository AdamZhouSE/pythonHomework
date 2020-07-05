def tran(a,r):
    for i in range(len(a)):
        res=[]
        k=i
        while not int(k+1) in res:
            res.append(k+1)
            k=a[k]-1
        res.append(k+1)
        res=find(res)
        r.append(res)
def find(x):
    res=[]
    res.append(x[len(x)-1])
    for i in range(len(x)):
        if  not x[len(x)-2-i]==x[len(x)-1]:
            res.append(x[len(x)-2-i])
        else:
            break
    return res
n=input()
a=[int(x) for x in input().split(" ")]
r=[]
tran(a,r)
count=len(r[0])
for i in range(len(r)):
    if count>len(r[i]):
        count=len(r[i])
print(count)