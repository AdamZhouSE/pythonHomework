n,m = input().split()
M = []
for x in range(int(n)):
    M.append(input())
startx = len(M)
endx = 0
for x in range(len(M)):
    if "B" in M[x] and startx == len(M):
        startx = x
    elif x > startx and "B" not in M[x]:
        endx = x - 1
        break
x = (startx + endx) // 2 + 1
starty = len(M[x - 1])
endy = 0
for y in range(len(M[x - 1])):
    if M[x - 1][y] == "B" and starty == len(M[x - 1]):
        starty = y
    elif y > starty and M[x - 1][y] != "B":
        endy = y - 1
        break
y = (starty + endy) // 2 + 1
print(x, y)
print(startx,endx)
print(starty,endy)
