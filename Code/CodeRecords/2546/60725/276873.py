p=list()
p.append(1)
p.append(1)
p.append(1)
for i in range(3,200):
    k=p[i-2]+p[i-3]
    p.append(k)
Y=int(input())
for j in range(Y):
    d=int(input())
    print(p[d])

