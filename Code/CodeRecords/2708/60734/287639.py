lst = list(map(int,input().split(' ')))
n, m, q = lst[0], lst[1], lst[2]
rooms = [set([]) for i in range(m)]
rooms[0] = set([i+1 for i in range(n)])
combs = []

for i in range(q):
    op, i, j = input().split(' ')
    if op == 'C':
        for index in range(len(rooms)):
            if int(i) in rooms[index]:
                rooms[index].remove(int(i))
                break
        rooms[int(j)-1].add(int(i))
    elif op == 'W':
        points = 0
        for index in range(int(i)-1, int(j)):
            if rooms[index] not in combs:
                combs.append(rooms[index].copy())
                points += len(rooms[index])
        print(points)