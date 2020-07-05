a=int(input())
b=[int(x) for x in input().split()]
c=[x for x in b]
c.sort()
position1=b.index(c[0]);position2=b.index(c[a-1])
little=min(position1,position2)
big=max(position1,position2)

print(max(big,a-1-little))