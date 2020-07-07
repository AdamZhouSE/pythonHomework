t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    s=input().split(' ')
    e=input().split(' ')
    if('' in s):
        s.remove('')
    if('' in e):
        e.remove('')
    for i in range(n):
        s[i]=int(s[i])
    for i in range(n):
        e[i]=int(e[i])
    s.sort()
    e.sort()
    m=1;o=1
    p=1;q=0
    while(p<n and q<n):
        if(int(s[p])<=int(e[q])):
            m+=1
            o=max(m,o)
            p+=1
        else:
            m-=1
            q+=1
    print(o)