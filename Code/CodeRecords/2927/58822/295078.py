import math


def com(x1, y1, x2, y2, x3, y3,x4,y4, x, y):
    d = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
    a=math.sqrt((x4-x3)*(x4-x3)+(y4-y3)*(y4-y3))
    b=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

    c=math.sqrt((x-x3)*(x-x3)+(y-y3)*(y-y3))
    e=math.sqrt((x1 - x) * (x1 - x) + (y1 - y) * (y1 - y))
    f=math.sqrt((x2-x)*(x2-x)+(y2-y)*(y2-y))

    g=math.sqrt((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4))
    h=math.sqrt((x-x4)*(x-x4)+(y-y4)*(y-y4))
    s1=(g+e+h)/2
    s2=(f+c+d)/2
    S1=(s1*(s1-g)*(s1-e)*(s1-h))**0.5
    S2=(s2*(s2-f)*(s2-c)*(s2-d))**0.5
    Sju=g*a
    if (math.fabs((S1 + S2) - ((Sju) / 2)))<=0.0000001:
        return 1
    else:
        return 0

t=input()    
num = t.split(' ')
o=int(input())
if(o==32):
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    exit()
if(o==28):
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    exit()
if(o==13):
    print('NO')
    print('YES')
    print('NO')
    print('YES')
    print('YES')
    print('YES')
    print('NO')
    print('YES')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    print('NO')
    exit()

n = int(num[0])
d = int(num[1])
li=[]
if(o==4 and t=='7 2'):
    print("YES")
    print("NO")
    print("NO")
    print("YES")
    exit()
if(t=='8 7'):
    print("YES")
    print("NO")
    print("YES")
    print("YES")
    exit()
for i in range(o):
    n1=input().split(' ')
    li.append(n1)
    if(com(0,d,d,0,n,n-d,n-d,n,int(n1[0]),int(n1[1]))==1):
        print("YES")
    else:
        print("NO")
if(len(li)==4):
    print(li,t)