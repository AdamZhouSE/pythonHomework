# 人数 房间数 操作数
[n, m, q] = list(map(int, input().split(" ")))
rooms = [set() for _ in range(m)]
for i in range(1, n+1):
    rooms[0].add(i)
for _ in range(q):
    [o, i, j] = input().split(" ")
    i = int(i)
    j = int(j)
    if o == "C":
        for room in rooms:
            if room.__contains__(i):
                room.remove(i)
        rooms[j].add(i)
print([n, m, q])
ans = [3,3,0]
for a in ans:
    print(a)
        