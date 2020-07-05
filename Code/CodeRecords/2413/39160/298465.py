from typing import List

n = int(input())
start = int(input())

def getList(n):
    if n == 1:
        return [0, 1]

    l = getList(n-1)
    return l + [x + (1<<(n-1)) for x in reversed(l)]

data = getList(n)
pos = -1
for i in range(1<<n):
    if start == data[i]:
        pos = i
        break
print(data[pos:] + data[: pos])
 