def is_interesting(x: list, s: int) -> bool:
    if len(x) % 2 == 1:
        return False
    else:
        return sum(x[:len(x) // 2]) <= s and sum(x[len(x) // 2:]) <= s


n, s = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(int(input()))
result = []
for i in range(len(data)):
    find = False
    for j in range(len(data), i, -1):
        if is_interesting(data[i:j], s):
            result.append(len(data[i:j]))
            find = True
            break
    if not find:
        result.append(0)
for i in result:
    print(i)
