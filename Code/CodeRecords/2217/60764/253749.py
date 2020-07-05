points=[]
for i in range(4):
    points.append(list(map(int,input().split(','))))
lines=[]
for i in range(3):
    for j in range(i+1,4):
        line=int(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2))
        if line not in lines:
            lines.append(line)
if len(lines)!=2:
    print(False)
elif max(lines)!=2*min(lines):
    print(False)
else:
    print(True)