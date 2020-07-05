
n = int(input())
distans = input().split(" ")
for i in range(n):
    distans[i] = int(distans[i])
points = input().split(" ")
points[0]=int(points[0])
points[1]=int(points[1])
points.sort()
res = []
all=0
for i in range(points[0],n):
    if(i!=points[1]-1):
        all+=distans[i]
    else:
        break
res.append(all)
distans =distans+distans
all=0
for i in range(points[1],2*n):
    if(i!=n+points[0]-1):
        all+=distans[i]
    else:
        break
res.append(all)
print(min(res))
