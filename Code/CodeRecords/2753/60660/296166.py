n=int(input())
l=eval(input())
src=int(input())
dist=int(input())
k=int(input())
dis=[10001 for _ in range(n)]
for i in range(len(l)):
    if l[i][0]==src:
        dis[l[i][1]]=l[i][2]
for i in range(1,k+1):
    for j in range(len(l)):
        dis[l[j][1]]=min(dis[l[j][1]],dis[l[j][0]]+l[j][2])
print(dis[dist])