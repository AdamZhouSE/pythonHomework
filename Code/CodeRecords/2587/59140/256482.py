n=int(input())
points=[]
time=0
for i in range(0,n):
    points.append(input().split(","))
for i in range(0,n-1):
    x_oriented=abs(int(points[i][0])-int(points[i+1][0]))
    y_oriented=abs(int(points[i][1])-int(points[i+1][1]))
    time+=max(x_oriented,y_oriented)
print(time)