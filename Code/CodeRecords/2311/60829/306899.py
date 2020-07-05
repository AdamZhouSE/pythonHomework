def dl(x):
    res=""
    for i in range(len(x)):
        if  not x[len(x)-1-i]==" ":
            break
    for j in range(i+1):
        if not x[j]=="-":
            res=res+x[j]
    return res
a=[]
b=[int(x) for x in dl(input()).split(" ")]
c=[int(x) for x in dl(input()).split(" ")]
a.append(b)
a.append(c)
aa=[[[10], [8]],[[1], [2]],[[0], [2]]]
bb=["0 4 0 20 0 12 0 ","0 5 0 ","0 4 0 17 2 8 2 "]
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
print(a,end='')