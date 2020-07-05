points=eval(input())
k=int(input())
d=[]
re=[]
for p in points:
    d.append(int(pow(p[0],2)+pow(p[1],2)))
for i in range(0,k):
    min_index=d.index(min(d))
    re.append(points[min_index])
    del points[min_index]
    del d[min_index]
print(re)