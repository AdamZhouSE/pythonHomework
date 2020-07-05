x = input()
xlist = x.split(" ")
n = int(xlist[0])
m = int(xlist[1])

aSet = set()
for i in range(n):
    x = input()
    xlist = x.split(" ")
    for j in range(1, 1 + int(xlist[0])):
        aSet.add(xlist[j])

if len(aSet) == m:
    print("YES")
else:
    print("NO")
