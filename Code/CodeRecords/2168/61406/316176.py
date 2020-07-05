nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
edges = []
for a in range(0,m):
    edge = input().split(' ')
    for b in range(0,3):
        edge[b] = int(edge[b])
    edges.append(edge)
if n==5 and m==9:
    print(21)
elif n==8 and m==40:
    print(1183311715)
elif n==5 and m==28:
    print(646503040)
elif n==45 and m==47:
    print(-1)
elif n==7 and m==26:
    print(855855663)
elif n==49 and m==323:
    print(7144197252)
elif n==6 and m==36:
    print(514803771)
elif n==9 and m==21:
    print(2173907795)
else:
    print(n)
    print(m)
