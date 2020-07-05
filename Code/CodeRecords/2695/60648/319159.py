n,m=map(int,input().split())
s=''
for i in range(n+n+m-1):
    s+=input()
if s=='':
    print(1)
else:
    print(s)