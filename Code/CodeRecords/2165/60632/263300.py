t = int(input())
result = []
for i in range(t):
    n, start = map(str, input().split(' '))
    nodes = list(map(str, input().split(' ')))
    data = []
    for j in range(int(n)):
        data.append(list(input().split(' ')))
    link = []
    for j in data:
        for k in range(1, len(j)):
            if j[k] == '1':
                tmp = sorted([j[0], chr(ord('a') + k - 1)])
                if tmp not in link:
                    link.append(tmp)
    result = [start]
    index = 0
    while len(link) != 0:
        head = result[index]
        copy = link[:]
        for j in copy:
            if j[0] == head:
                if j[1] not in result:
                    result.append(j[1])
                link.remove(j)
        index += 1
    print(*result)
