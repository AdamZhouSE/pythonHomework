def line(p1,p2,p3):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

s = input().split(' ')
n = int(s[0])
d = int(s[1])
p1 = [0,d]
p2 = [d,0]
p3 = [n,n - d]
p4 = [n - d,n]
m = int(input())
for i in range(0,m):
    p5 = list(map(int,input().split(' ')))
    if(line(p1,p2,p5) >= 0 and line(p2,p3,p5) >= 0 and line(p4,p3,p5) <= 0 and line(p1,p4,p5) <= 0):       
        print('YES')
    else:
        print('NO')