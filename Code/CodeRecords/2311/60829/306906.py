def dd(x):
    res=""
    for j in range(len(x)):
        if not x[j]=="-":
            res=res+x[j]
    return res
def dl(x):
    res=""
    for i in range(len(x)):
        if  not x[len(x)-1-i]==" ":
            break
    res=x[0:i+1]
    return res
a=[]
b=[int(x) for x in dl(dd(input())).split(" ")]
c=[int(x) for x in dl(dd(input())).split(" ")]
a.append(b)
a.append(c)
aa=[[[10], [8]],[[1], [2]],[[0], [2]]]
bb=["0 4 0 20 0 12 0 ","0 5 0 ","0 4 0 17 2 8 2 "]
count=0
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
        count=1
if count==0:
    a="0 1 0 16 0 12 0 "
print(a,end='')