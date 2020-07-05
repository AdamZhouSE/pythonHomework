n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split(','))
    points.append((x,y))
ans=0
for i in range(n-1):
    ans+=max(abs(points[i][1]-points[i+1][1]),abs(points[i][0]-points[i+1][0]))
print(ans)