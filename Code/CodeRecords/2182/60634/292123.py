def go(arr, i, k):
    if i == len(arr):
        i = 0
    k -= 1
    while k != 0:
        i = (i + 1) % len(arr)
        k -= 1
    return i


def solve(n, k):
    arr = [x for x in range(n)]

    i = 0
    while len(arr) > 1:
        i = go(arr, i, k)
        arr.remove(arr[i])

    return arr[0] + 1


# main-----
p = int(input())
for x in range(p):
    temp = input().split(' ')
    n = int(temp[0])
    k = int(temp[1])

    print(solve(n, k))
































