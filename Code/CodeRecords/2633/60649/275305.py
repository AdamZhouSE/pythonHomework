n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(m):
    s=input()
    if s[0]=='1':
        c,L,R,K,D=map(int,s.split())
        while L<=R:
            a[L-1]+=K
            K+=D
            L+=1
    else:
        c,k=map(int,s.split())
        print(a[k-1])