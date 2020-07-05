a=[]
b=[int(x) for x in input().split(" ")]
c=[int(x) for x in input().split(" ")]
a.append(b)
a.append(c)
aa=[]
bb=[]
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
print(a)