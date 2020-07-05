n = int(input())
li = []
xaxis = []
maxX = 0
for i in range(n):
    x = input().strip().split()
    li.append([int(x[0]), int(x[1]), int(x[2])])
    maxX = max(maxX, max(int(x[0]), int(x[1])))
xaxis = [0 for i in range(maxX)]
for i in li:
    ai = i[0]
    bi = i[1]
    hi = i[2]
    for j in range(ai-1, bi-1):
        xaxis[j] = max(xaxis[j], hi)
height = 0
for i in xaxis:
    height += i
# print(xaxis)
print(height)
