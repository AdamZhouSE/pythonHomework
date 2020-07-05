R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
lists = [[0 for i in range(C)] for j in range(R)]
locations = list()
distance = list()
for i in range(R):
    for j in range(C):
        locations.append([i,j])
        distance.append(abs(i-r0)+abs(j-c0))
uses = list(zip(locations,distance))
uses.sort()
sortlist = sorted(uses,key=lambda quality:quality[1])
ans = list()
for i in sortlist:
    ans.append(i[0])
print(ans)