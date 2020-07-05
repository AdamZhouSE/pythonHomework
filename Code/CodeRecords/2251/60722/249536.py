n=int(input())
coord=[]
for i in range(n):
    string=input().split(",")
    coordi=[int(string[0]),int(string[1])]
    coord.append(coordi)
area=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            area.append((coord[j][0]-coord[i][0])*(coord[j][1]-coord[i][1])/2+
                        (coord[k][0]-coord[j][0])*(coord[j][1]-coord[i][1])/2+
                        (coord[j][0]-coord[i][0])*(coord[i][1]-coord[k][1])/2)
area.sort()
print(area[len(area)-1])