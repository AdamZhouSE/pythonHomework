def IsTrangleOrArea(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
 
def IsInside(x1,y1,x2,y2,x3,y3,x,y):
    #三角形ABC的面积
    ABC = IsTrangleOrArea(x1,y1,x2,y2,x3,y3)
    # 三角形PBC的面积
    PBC = IsTrangleOrArea(x,y,x2,y2,x3,y3)
    # 三角形ABC的面积
    PAC = IsTrangleOrArea(x1,y1,x,y,x3,y3)
    # 三角形ABC的面积
    PAB = IsTrangleOrArea(x1,y1,x2,y2,x,y)
    return (ABC == PBC + PAC + PAB) and (y1-y2)*(x-x1)!= (y-y1)*(x1-x2) and (y3-y2)*(x-x2)!= (y-y2)*(x3-x2) 

t = int(input());
for i in range(t):
    line = input().split(' ');
    x1 = int(line[0]);
    y1 = int(line[1]);
    line = input().split(' ');
    x2 = int(line[0]);
    y2 = int(line[1]);
    line = input().split(' ');
    x3 = int(line[0]);
    y3 = int(line[1]);
    minx = min(x1, x2, x3);
    maxx = max(x1, x2, x3);
    miny = min(y1, y2, y3);
    maxy = max(y1, y2, y3);
    count = 0;
    for j in range(minx+1, maxx):
        for k in range(miny+1, maxy):
            if IsInside(x1,y1,x2,y2,x3,y3,j,k):
                count+=1;
    print(count);
 