equations = [[x[1], x[2], x[4]] for x in input()[1:-1].split(",")]
values = {chr(i) : chr(i) for i in range(ord('a'), ord('z') + 1)}
def find(i):
    if i != values[i]:
        values[i] = find(values[i])
    return values[i]


flag = 'true'
for e in equations:
    if e[1] == '=':
        values[find(e[0])] = find(e[-1])
    elif e[1] == '!':
        if find(e[0]) == find(e[1]):
            flag = 'false'
            break
print(flag)
