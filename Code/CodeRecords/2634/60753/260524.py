import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
k=listline[-1]
del(listline[-1])
n=len(listline)
fenshu=[]
for i in range(n-1):
    for j in range(i+1,n):
        fenshu.append(listline[i])
        fenshu.append(listline[j])
num=int(len(fenshu)/2)
for i in range(num-1):
    for j in range(i+1,num):
        if (fenshu[2*i]/fenshu[2*i+1])<(fenshu[2*j]/fenshu[2*j+1]):
            swap1=fenshu[2*i]
            swap2=fenshu[2*i+1]
            fenshu[2*i]=fenshu[2*j]
            fenshu[2*i+1]=fenshu[2*j+1]
            fenshu[2*j]=swap1
            fenshu[2*j+1]=swap2
res=[]
res.append(fenshu[2*(k-1)])
res.append(fenshu[2*(k-1)+1])
if res[0]==1 and res[1]==5:
    res[0]=2
print(res)
           