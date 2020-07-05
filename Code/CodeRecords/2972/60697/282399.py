t = int(input())
a = []
b = []
for i in range(t):
    a.append(list(input()))
    b.append(list(input()))
s=True
for i in range(t):
    e=a[i]
    f=b[i]
    c=[]
    d=[]
    for j in range(len(e)):
        if(e[j]!=' '):
            c.append(e[j])
    for j in range(len(f)):
        if(f[j]!=' '):
            d.append(f[j])
    s = True
    if(len(c)==0 and len(d)==0):
        s=True
    elif(len(c)==0 and len(d)!=0):
        s=False
    elif(c[0]!=d[0]):
        s=False
    elif(len(c)>1 and len(d)>1 and c[1]!=d[1] and c[0]==d[1]):
        s=False
    else:
        for j in range(1,len(d)):
            if(j<len(c)):
                if(c[j]!=d[j]):
                    if(c[:j]==[d[j] for i in range(j)] and c[j-1]==d[j]):
                        s=False
                        break
                    c.insert(j,d[j])
            else:
                if(d[j]==c[-1]):
                    s=False
                    break
                c.append(d[j])
    if(s):
        print("Yes")
    else:
        print("No")







