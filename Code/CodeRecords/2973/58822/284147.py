def spaixu(a):
    o = list(a)
    o.sort()
    k = "".join(o)
    return k
n=input()
num=int(input())
l=[]
for i in range(num):
    k=input()
    l.append(spaixu(k))
ta=[]
for i in range(0,len(n)-7):
    p=n[i:(i+8)]
    ta.append(spaixu(p))
res=0
for k in range(num):
    for i in range(len(ta)):
        if(l[k]==ta[i]):
            res+=1
print(res)