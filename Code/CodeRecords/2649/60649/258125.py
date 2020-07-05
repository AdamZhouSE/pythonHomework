T=int(input())
for i in range(T):
    N,L,R=map(int,input().split())
    s="{0:b}".format(N)
    s=list(s)
    for i in range(L,R+1):
        s[-i]='0' if s[-i]=='1' else '1'
    s="".join(s)
    print(int(s,2))