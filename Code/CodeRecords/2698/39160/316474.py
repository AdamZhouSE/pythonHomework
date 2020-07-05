s=input()
n=0
d=0
i=0
while(s[i]!=' '):
    n=n*10+int(s[i])
    i=i+1
i=i+1
while(i<len(s)):
    d=d*10+int(s[i])
    i=i+1
f=[1]
if(d==0):
    print(1, end='')
else:
    i=1
    while(i<=d):
        f.append(f[i-1]**n+1)
        i=i+1
    print(f[d]-f[d-1], end='')