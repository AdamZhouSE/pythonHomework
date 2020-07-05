def new_sorted(s):
    a=sorted(s)
    b=list(set(a))
    c=[]
    for i in range(len(b)):
        d=[]
        d.append(a.count(b[i]))
        d.append(b[i])
        c.append(d)
    c.sort()
    result=[]
    for i in range(len(c)):
        for j in range(c[i][0]):
            result.append(c[i][1])
    return result

S=input()
s=new_sorted(S)
n=len(s)//2
if s[n-1]==s[-1]:
    print("")
else:
    a,b=s[:n],s[n:]
    for i in range(len(b)):
        s[i*2]=b[i]
    for i in range(len(a)):
        s[i*2+1]=a[i]
    print("".join(s))
