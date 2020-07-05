def f(s,t):
    if len(s)>len(t):
        for i in range(len(s)-len(t)):
            t='0'+t
    if len(t)>len(s):
        for i in range(len(t)-len(s)):
            s='0'+s
    a=list(s)
    b=list(t)
    a.reverse()
    b.reverse()
    Cn=0
    Sn=0
    result=[]
    for i in range(0,len(a)):
        Sn=(Cn+int(a[i])+int(b[i]))%2
        Cn=int((Cn+int(a[i])+int(b[i]))/2)
        result.append(str(Sn))
    if Cn!=0:
        result.append('1')
    result.reverse()
    return ''.join(result)


s=input().strip()
t=input().strip()
print(f(s,t))
    