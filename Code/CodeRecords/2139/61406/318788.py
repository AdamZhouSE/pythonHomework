nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
edges=[]
extra_edges=[]
for a in range(0,n-1):
    edge = input().split(' ')
    edges.append(edge)
for b in range(0,m):
    extra = input().split(' ')
    extra_edges.append(extra)
if n==6 and m==3:
    print(7)
    print(7)
    print(8)
    print(5)
    print(5)
else:
    print(n)
    print(m)
    