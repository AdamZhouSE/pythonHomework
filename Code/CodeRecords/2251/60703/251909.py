n  = int(input());
list = [];
for i in range(n):
    list.append([int(x) for x in input().split(",")])
maxArea = 0;

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1 = list[i][0],list[i][1];
            x2, y2 = list[j][0], list[j][1];
            x3, y3 = list[k][0], list[k][1];

            tempArea = abs(x1*y2-x2*y1+x2*y3-x3*y2+x3*y1-x1*y3)/2
            if(tempArea>maxArea):
                maxArea = tempArea
print(maxArea)