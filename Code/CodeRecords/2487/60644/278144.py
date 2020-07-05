t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    s=list(set(a))
    p=[]+s
    b=[]
    for j in range(0,len(s)):
        s[j]=a.count(s[j])
    for j in range(0,len(s)):
        if s[j]==max(s):
            b=b+[j]
    for k in range(0,len(b)):
        b[k]=p[b[k]]
    print(min(b)+' '+str(a.count(min(b))))
