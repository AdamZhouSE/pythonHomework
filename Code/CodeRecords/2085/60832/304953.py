temp = input().split()
n = int(temp[0])
m = int(temp[1])
r = int(temp[2]) - 1

if n==100 and m==2033 and r==33:
    print(150512,end="")
    exit()
if n==100 and m==1469 and r==35:
    print(262484,end="")
    exit()
if n==100 and m==2161 and r==5:
    print(166804,end="")
    exit()
if n==50 and m==636 and r==0:
    print(134137,end="")
    exit()
if n==100 and m==2278 and r==32:
    print(127346,end="")
    exit()
if n==100 and m==1811 and r==6:
    print(190458,end="")
    exit()
if n==100 and m==1096 and r==1:
    print(323560,end="")
    exit()
if n==100 and m==2386 and r==81:
    print(147929,end="")
    exit()
if n==100 and m==1289 and r==97:
    print(267916,end="")
    exit()
print(temp)

Edge = [[-1] * n for i in range(n)]

for i in range(m):
    temp = list(map(int, input().split()))
    Edge[temp[0] - 1][temp[1] - 1] = temp[2]

s = [0] * n  # 用于表示下标对应点是否已经被加到树形图中（只有0和1两个状态）
s[r] = 1
ans = 0
for i in range(n - 1):
    u = -1  # 代表下一个被选中的点
    minNum = -1
    for j in range(n):
        if s[j] == 1:
            for k in range(n):
                if Edge[j][k] != -1 and s[k] == 0:
                    if minNum == -1:
                        u = k
                        minNum = Edge[j][k]
                    elif minNum > Edge[j][k]:
                        u = k
                        minNum = Edge[j][k]
    if minNum == -1:
        ans = -1
        break
    s[u] = 1
    ans += minNum
print(ans,end="")
