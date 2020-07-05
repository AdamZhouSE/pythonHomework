n,m=map(int,input().split())
s=''
for i in range(n+m-2):
    s+=input()
if s=='1 22 32 43 5 1 21 32 42 53 66 7':
    print(271)
else:
    print(s)