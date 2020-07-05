a=int(input())
b=[int(x) for x in input().split()]
c=set();
for x in b:
    if x!=0:
        c.add(x)

print(len(c))