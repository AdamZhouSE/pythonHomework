L,T,O=map(int,input().split())
a=[1]*L


for i in range(O):
    s=list(input().split())
    if s[0]=='C':
        A,B,C=int(s[1]),int(s[2]),int(s[3])
        if A>B:
            A,B=B,A
        for j in range(A-1,B):
            a[j]=C
    if s[0]=="P"or s[0]=='p':
        A,B=int(s[1]),int(s[2])
        if A>B:
            A,B=B,A
        S=set(a[A-1:B])
        print(len(S))
