R = int(input())
C  =int(input())
r0 = int(input())
c0 = int(input())

distList = [[] for x in range(200)]
for i in range(R):
    for j in range(C):
        distance = abs(r0-i)+abs(c0-j)
        distList[distance].append([i,j])
res = []
for i in distList:
    for j in i:
        res.append(j)
print(res)