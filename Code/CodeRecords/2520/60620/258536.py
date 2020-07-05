r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
distance=[[] for i in range(200)]
for i in range(r):
    for j in range(c):
        d=abs(r0-i)+abs(c0-j)
        distance[d].append([i,j])
result=[]
for i in distance:
    if i:
        result.extend(i)
print(result)
        