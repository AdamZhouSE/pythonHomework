n,m=map(int,input().split())
s=set()
for i in range(n):
    s.update(map(int,input().split()[1:]))
if len(s)==m:
    print('YES')
else:
    print('NO')