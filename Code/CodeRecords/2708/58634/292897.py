n, m, q = map(int, input().split(" "))
groups = []
people = []
room = []  # 存每个房间的人的编号
for i in range(m + 1):
    room.append([])
people.append(0)
for i in range(n):
    people.append(1)  # 表示一开始在的房间
    room[1].append(i + 1)
for i in range(q):
    order, a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if order == "C":
        room[people[a]].remove(a)
        people[a] = b
        room[b].append(a)
    else:
        res = 0
        for k in range(a, b + 1):
            if room[k] != []:
                if tuple(room[k]) in groups:
                    continue
                else:
                    res += len(room[k])
                    groups.append(tuple(room[k]))
        print(res)
