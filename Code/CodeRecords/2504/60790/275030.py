points=eval(input())
k=int(input())
ans=[]
for point in points:
    ans.append(point[0]**2+point[1]**2)
result=[]
for i in range(0,k):
    min1=min(ans)
    result.append(points[ans.index(min1)])
    ans.remove(min1)
print(result)