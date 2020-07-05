n = int(input())
li = []
for i in range(n):
    k = input().strip().split(",")
    t = [int(k[0]), int(k[1])]
    li.append(t)

x1 = li[0][0]
y1 = li[0][1]
x2 = li[1][0]
y2 = li[1][1]

k = 0
if x1 != x2:
    k = (y1-y2)/(x1-x2)
b = y1-k*x1
if n == 2:
    print("True")
else:
    isOK = True
    for i in range(3, n):
        y = li[i][1]
        x = li[i][0]
        if (y != k*x+b):
            isOK = False
            break
    print(isOK)