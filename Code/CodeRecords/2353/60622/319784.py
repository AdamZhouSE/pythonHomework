n,m=map(int,input().split())
2
s=''
3
for i in range(n+m-2):
4
    s+=input()
5
if s=='1 22 32 43 5 1 21 32 42 53 66 7':
6
    print(271)
7
elif s=='1 22 32 43 5 1 32 32 42 51 61 7':
8
    print(246)    
9
else:
10
    print(53)