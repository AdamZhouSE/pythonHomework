L,T,O=map(int,input().split())
y=[1 for i in range(L)]
for i in range(O):
    s=input().split()
    if(s[0]=='C'):
        a=int(s[1])
        b=int(s[2])
        if(a>b):
            b=int(s[1])
            a=int(s[2])
        c=int(s[3])
        for j in range(a-1,b):
            y[j]=c
    else:
        a=int(s[1])
        b=int(s[2])
        if(a>b):
            b=int(s[1])
            a=int(s[2])
        print(len(set(y[a-1:b])))
        