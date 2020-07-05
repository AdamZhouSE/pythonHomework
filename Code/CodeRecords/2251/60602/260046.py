import numpy as np
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def maxTriangle(Point):
    i=0;
    ans=[];
    while(i<len(Point)):
        PointList = [];
        PointList.append(Point[i]);
        j=i+1;
        while(j<len(Point)):
            PointList.append(Point[j]);
            x=j+1;
            while(x<len(Point)):
                PointList.append(Point[x]);
                temp=np.array(PointList);
                ans.append(abs(0.5*np.linalg.det(temp)));
                PointList.remove(PointList[len(PointList)-1]);
                x+=1;
            PointList.remove(PointList[len(PointList) - 1]);
            j+=1;
        PointList.remove(PointList[len(PointList) - 1]);
        i+=1;
    print(max(ans));




Total=int(input());
i=0;
Point=[];
while(i<Total):
    list=str(input());
    list=makeIntList(list.split(","));
    list.append(1);
    Point.append(list);
    i+=1;
maxTriangle(Point);