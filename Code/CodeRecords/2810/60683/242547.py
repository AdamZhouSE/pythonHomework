n = eval(input())
size = len(str(n))
level = [0] * size
allZero = [0] * size
for i in range(size):
    level[i] = n % 10
    n = n // 10
# print(level)
res = []
while True:
    i = size - 1
    component = 0
    while i >= 0:
        if level[i] != 0:
            component += 10 ** i
            level[i] -= 1
        i -= 1
    res.append(component)
    if level == allZero:
        break
print(len(res))
print(*res)
