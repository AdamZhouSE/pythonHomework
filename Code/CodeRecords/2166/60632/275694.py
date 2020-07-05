def next_index(sign: list, x: int, begin: int) -> int:
    while x != 0:
        begin = (begin + 1) % len(sign)
        if sign[begin] == 0:
            x -= 1
    return begin


t = int(input())
result = []
for i in range(t):
    n = int(input())
    arr = [0 for j in range(n)]
    index = -1
    for k in range(1, n + 1):
        index = next_index(arr, k + 1, index)
        arr[index] = k
    result.append(arr)
for i in result:
    print(*i)
