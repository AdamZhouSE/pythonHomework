t=input().split()
M=int(t[0])
D=int(t[1])
a=[]
n=0
for i in range(0,M):
    s=input().split()
    if s[0]=='A':
        p=(n+int(s[1]))%D
        a=a+[p]
    else:
        b=a[-int(s[1]):]
        b.sort(reverse=True)
        n=b[0]
        print(b[0])

