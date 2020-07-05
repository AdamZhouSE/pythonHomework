n = int(input())
instructions = []
for i in range(n):
    instructions.append(list(map(str, input().split(' '))))
exps = []
result = []
for i in instructions:
    if i[0] == 'Add':
        exps.append(list(map(int, i[1:])))
    elif i[0] == 'Del':
        tmp = 0
        for j in instructions:
            if j[0] == 'Add':
                tmp += 1
            if tmp == int(i[1]):
                exps.remove(list(map(int, j[1:])))
                break
    elif i[0] == 'Query':
        x = int(i[1])
        count = 0
        for e in exps:
            if e[0] * x + e[1] > e[2]:
                count += 1
        result.append(count)
print(result)
