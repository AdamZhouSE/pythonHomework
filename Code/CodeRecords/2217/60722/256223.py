Coordinate=[]
for i in range(4):
    string=input().split(",")
    Coordinate.append([int(string[0]),int(string[1])])
Distance=[]
for i in range(4):
    for j in range(4):
        if i!=j:
            a=abs(Coordinate[i][0]-Coordinate[j][0])
            b=abs(Coordinate[i][1]-Coordinate[j][1])
            Distance.append(a*a+b*b)
Distance=list(set(Distance))
Distance.sort()
print(len(Distance)==2 and 2*Distance[0]==Distance[1])