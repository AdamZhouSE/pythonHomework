def vector(a,b):
    return[b[0]-a[0],b[1]-a[1]]
def cross(a,b):
    return a[0]*b[1]-b[0]*a[1]
n,m=map(int,input().strip().split(' '))
a=[0,m]
b=[m,0]
c=[n,n-m] if m<0 else[n-m,n]
d=[n-m,n] if m<0 else[n,n-m]
ab=vector(a,b)
dc=vector(d,c)
ca=vector(c,a)
bd=vector(b,d)
enemy_nums=(int)(input())
enemies=[]
for i in range(enemy_nums):
    enemies.append(list(map(int,input().strip().split(' '))))
for i in enemies:
    ai=vector(a,i)
    bi=vector(b,i)
    ci=vector(c,i)
    di=vector(d,i)
    if(cross(ab,ai)*cross(dc,di)>=0 and cross(ca,ci)*cross(bd,bi)>=0):
        print('YES')
    else:
        print('NO')
