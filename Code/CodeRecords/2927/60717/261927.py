tmp=input().split()
n=int(tmp[0])
d=int(tmp[1])
m=int(input())
for i in range(0,m):
    tmp=input().split()
    x=int(tmp[0])
    y=int(tmp[1])
    if x+y>=d and x+y<=2*n-d and y-x<=d and x-y<=d:
        print('YES')
    else:
        print('NO')