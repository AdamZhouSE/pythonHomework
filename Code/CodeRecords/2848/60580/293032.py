a = input()
select = input().split()
aL = input().split()
bL = input().split()
x = 0
while x < len(aL):
    aL[x] = int(aL[x])
    x += 1
y = 0
while y < len(bL):
    bL[y] = int(bL[y])
    y += 1
aL.sort()
bL.sort()
if int(aL[int(select[0]) - 1]) < int(bL[len(bL) - int(select[1])]):
    print("YES")
else:
    print("NO")