N,P=map(int,input().split())
a=list(map(int,input().split()))
M=int(input())
for i in range(M):
    s=list(map(int,input().split()))
    if s[0]==1:
        for i in range(s[1]-1,s[2]):
            a[i]*=s[3]
    if s[0]==2:
        for i in range(s[1]-1,s[2]):
            a[i]+=s[3]
    if s[0]==3:
        print(sum(a[s[1]-1:s[2]])%P)