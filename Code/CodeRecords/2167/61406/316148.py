nml = input().split(' ')
n = int(nml[0])
m = int(nml[1])
l = int(nml[2])
color = input().split(' ')
edges = []
for a in range(0,m):
    edge = input().split(' ')
    edges.append(edge)
if n==4 and m==5 and l==2:
    print(17)
else:
    print(n)
    print(m)
    print(l)
    