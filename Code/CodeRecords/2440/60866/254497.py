def paixu(a):
    b=[]
    b.append(a[0])
    for i in range(1,len(a)):
        for j in range(0,len(b)):
            if a[i]<b[j]:
                b.insert(j,a[i])
                break
            if(j==len(b)-1):
                b.append(a[i])
    print(b)
a=input()
a=list(a)
b=[]
for x in a:
    if x.isdigit():
        b.append(x)
b=[int(x) for x in b]
paixu(b)