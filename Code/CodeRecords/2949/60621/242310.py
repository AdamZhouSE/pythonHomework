a=[int(x) for x in input().split()]
a.pop()
for i in a[::-1]:
    print(i,end=" ")
