n,d=map(int,input().split(' '))
m=int(input())
for i in range(m):
    x,y=map(int,input().split(' '))
    if x+y>=d and x+y<=2*n-d and y-x>=-d and y-x<=d:
        print('YES')
    else:
        print('NO')
