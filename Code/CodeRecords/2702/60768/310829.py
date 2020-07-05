net = []
for i in range(0, 4):
    a = list(input())
    a = [int(u) for u in a]
    net.append(a)


def func(i, j, count):
    if i < 0 or j < 0 or i >= 4 or j >= 5 or net[i][j] != 1:
        return
    net[i][j] = count
    func(i + 1, j, count)
    func(i, j + 1, count)
    func(i - 1, j, count)
    func(i, j - 1, count)


count = 2
for i in range(0, 4):
    for j in range(0, 5):
        if net[i][j] == 1:
            func(i, j, count)
            count += 1
re = 0
for i in range(4):
    for j in range(5):
        if net[i][j] > re:
            re = net[i][j]
print(re - 1)