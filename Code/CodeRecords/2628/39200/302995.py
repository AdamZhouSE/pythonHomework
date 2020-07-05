def crossproduct(p1, p2):
    return p1[0]*p2[1]-p1[1]*p2[0]

def cal(p, q, r):
    count = 0
    maxx = max(p[0], q[0], r[0])
    maxy = max(p[1], q[1], r[1])
    minx = min(p[0], q[0], r[0])
    miny = min(p[1], q[1], r[1])
    for x in range(minx,maxx+1):
        for y in range(miny,maxy+1):
            xp=[x-p[0],y-p[1]]
            xq=[x-q[0],y-q[1]]
            xr=[x-r[0],y-r[1]]
            t1 = crossproduct(xp, xq)
            t2 = crossproduct(xq, xr)
            t3 = crossproduct(xr, xp)
            if t1*t2>0 and t2*t3>0:
                count += 1
    return count
    
    
t = int(input())
for x in range(t):
    p = input().split(" ")
    q = input().split(" ")
    r = input().split(" ")
    print(cal([int(p[0]), int(p[1])], [int(q[0]), int(q[1])], [int(r[0]), int(r[1])]))
