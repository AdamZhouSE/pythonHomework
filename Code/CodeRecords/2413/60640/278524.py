n = int(input())
start = int(input())
grayList = []
index = 0
for i in range(1 << n):
    grayList.append(i ^ i >> 1)
    if i ^ i >> 1 == start:
        index = i
res = grayList[index:len(grayList)] + grayList[0:index]
print("[", end="")
for i in range(len(res)-1):
    print(res[i], end=", ")
print(res[len(res)-1], end="]")
print()

