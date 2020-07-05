alen,blen=map(int,input().split())
a=input().split()
b=input().split()
result=[]
for i in range(alen):
    a[i]=int(a[i])
for i in range(blen):
    b[i]=int(b[i])
a.sort()
for m in range(blen):
    for n in range(alen):
        if b[m]<a[n]:
            result.append(str(n))
            break
    else:
        result.append(str(n+1))
s=(" ").join(result)
print(s)