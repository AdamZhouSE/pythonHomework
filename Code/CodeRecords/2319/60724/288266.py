Coordinate=[]
N=int(input())
for i in range(N):
    coor=[]
    string=input().split(",")
    for j in range(N):
        coor.append(int(string[j]))
    Coordinate.append(coor)
area=0
for i in range(N):
    for j in range(N):
        if Coordinate[i][j]!=0:
            area+=2
for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            area=area+4*Coordinate[i][j]
        elif i==0 and j!=0:
            area=area+4*Coordinate[i][j]-2*min(Coordinate[i][j-1],Coordinate[i][j])
        elif j==0 and i!=0:
            area=area+4*Coordinate[i][j]-2*min(Coordinate[i-1][j], Coordinate[i][j])
        else:
            area=area+4*Coordinate[i][j]-2*min(Coordinate[i-1][j],Coordinate[i][j])-2*min(Coordinate[i][j-1],Coordinate[i][j])
print(area)