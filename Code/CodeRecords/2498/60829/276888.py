x=str(input())
y=[int(i) for i in x[1:len(x)-1].split(",")]
a=[]
b=[]
for i in y:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
a.sort()
b.sort()
res=[]
for i in range(len(a)):
    res.append(a[i])
    res.append(b[i])
print(res)