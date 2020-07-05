s=input()
sl=s.split( )
n=int(sl[0])
d=int(sl[1])
h=(n-d)
w=d/2
emn=int(input())
for i in range(emn):
    m=input()
    ml=m.split( )
    x=int(ml[0])-d/2
    y=int(ml[1])-d/2
    tempx=1/2*x-1/2*y
    tempy=x*1/2+y/2
    if(tempx>=-w and tempx<=w and tempy<=h and tempy>=0):
        print('YES')
    else:
        print('NO')
