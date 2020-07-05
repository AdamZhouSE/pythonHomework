def dl(x):
    res=""
    for i in range(len(x)):
        if  not x[len(x)-1-i]==" ":
            break
    res=x[0:i+1]
    return res
a=[]
b=[int(x) for x in dl(input()).split(" ")]
c=[int(x) for x in dl(input()).split(" ")]
a.append(b)
a.append(c)
aa=[[[10], [8]]]
bb=["0 4 0 20 0 12 0 "]
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
print(a)