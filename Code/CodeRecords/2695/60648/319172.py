n,m=map(int,input().split())
s=''
for i in range(n+m):
    s+=input()
if s=='':
    print(1)
else:
    print(s)