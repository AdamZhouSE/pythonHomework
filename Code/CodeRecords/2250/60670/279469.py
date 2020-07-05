def getline(point1,point2):
    #直线一般式Ax+By+C=0
    #A=y2-y1,B=x1-x2,C=x2y1-x1y2
    return (point2[1]-point1[1],point1[0]-point2[0],point2[0]*point1[1]-point1[0]*point2[1])

def inline(point,line):
    if line[0]*point[0]+line[1]*point[1]+line[2]==0:
        return True
    else:
        return False

n=int(input())
points=[]
for i in range(0,n):
    x,y=map(int,input().split(','))
    points.append([x,y])
line_dic={}
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            line=getline(points[i],points[j])
            if not(line in line_dic):
                linedic[line]=0
maxn=0
for point in points:
    for line in line_dic.keys():
        if inline(point,line):
            line_dic[line]+=1
            maxn=max(maxn,line_dic[line])
print(maxn)