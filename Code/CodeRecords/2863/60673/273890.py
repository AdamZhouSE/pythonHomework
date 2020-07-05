# 围墙高h 第i个人高a[i] 平常走路宽度为1 弯腰2
inp = input()
n = int(inp[0])
h = int(inp[2])
a = input().split(" ")
for i in range(n):
    a[i] = int(a[i])
walkNum = 0
bendNum = 0
for i in range(n):
    if (a[i] > h):
        bendNum += 1
    else:
        walkNum += 1
print(walkNum + bendNum * 2)
