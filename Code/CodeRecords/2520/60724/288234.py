R,C,r0,c0=int(input()),int(input()),int(input()),int(input())
dist=[[] for i in range(R+C)]
for i in range(R):
    for j in range(C):
        dist[abs(r0-i)+abs(c0-j)].append([i,j])
result=[]
for i in dist:
    if i:
        result.extend(i)
    else:
        break
print(result)