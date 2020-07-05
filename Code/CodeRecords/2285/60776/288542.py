a=int(input())
for k in range(0,a):
    a=input()
    shangzhang=0
    xiadie=1
    c=[]
    d=[]
    b = input().split(' ')
    for i in range(0, len(b)):
        b[i] = int(b[i])
    for i in range(0,len(b)-1):
        if xiadie==1 and b[i+1]>b[i]:
            d.append(i)
            shangzhang=1
            xiadie=0
        if shangzhang==1 and b[i+1]<b[i]:
            d.append(i)
            c.append(d)
            d=[]
            xiadie=1
            shangzhang=0
    if d!=[] :
        d.append(len(b)-1)
        c.append(d)
    result=[]
    for i in range(0,len(c)):
        result.append("("+' '.join(str(j) for j in c[i])+")")
    print(' '.join(result))