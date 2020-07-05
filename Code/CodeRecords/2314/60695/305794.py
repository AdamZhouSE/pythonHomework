n = int(input())
b = []
for i in range(n):
    l = input().split(" ")
    l = list(map(int, l))
    if l[0] not in b:
        b.append(l[0])
    ind = b.index(l[0])
    if l[1] != 0:
        b.insert(ind, l[1])
    ind = b.index(l[0])
    if l[2] != 0:
        b.insert(ind + 1, l[2])
    if n == 3 and i == 0:
        break
for i in range(0, len(b)):
    print(str(b[i])+ " " , end="")

