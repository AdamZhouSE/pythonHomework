R,C,r0,c0=int(input()),int(input()),int(input()),int(input())
2
dist=[[] for i in range(R+C)]
3
for i in range(R):
4
    for j in range(C):
5
        dist[abs(r0-i)+abs(c0-j)].append([i,j])
6
result=[]
7
for i in dist:
8
    if i:
9
        result.extend(i)
10
    else:
11
        break
12
print(result)