import re
n = int(input())
#n = 4
lst = list(map(int, re.findall(r'\d+', input())))
#lst = [1,0,2,0,3,1,3,2]
edges = []
for i in range(len(lst) // 2):
    edges.append([lst[2 * i+1], lst[2 * i]])
edges.sort(key=lambda x:(x[0],x[1]))
lesson = {}
for i in range(n):
    lesson[i] = 0
for e in edges:
    lesson[e[1]]+=1

route = []
q = []
for k,v in lesson.items():
    if v == 0:
        q.append(k)
while q:
    le = q.pop(0)
    route.append(le)
    for e in edges:
        if e[0] == le:
            lesson[e[1]]-=1
            if lesson[e[1]] == 0:
                q.append(e[1])
print(route)