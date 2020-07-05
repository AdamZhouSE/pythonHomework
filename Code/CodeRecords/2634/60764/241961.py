from fractions import Fraction
a=eval(input())
k=int(input())
frac=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        frac.append(Fraction(a[i],a[j]))
frac.sort()
res=list(map(int,str(frac[k-1]).split("/")))
res1=res.copy()
count=2
while (res1[0] not in a) or (res1[1] not in a):
    res1[0]=count*res[0]
    res1[1]=count*res[1]
    count+=1
print(res1)