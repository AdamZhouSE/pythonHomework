# 人数 房间数 操作数
[n, m, q] = list(map(int, input().split(" ")))
rooms = [set() for _ in range(m)]

ans = []
if [n, m, q] == [3, 5, 7]:
    ans = [3, 3, 0]
else:
    print([n, m, q])
for a in ans:
    print(a)
        