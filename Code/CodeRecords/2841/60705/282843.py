def solve(arr):
    count = 0
    while len(arr) > 1:
        t = arr.copy()
        arr = []
        if count % 2 == 0:
            for j in range(0, len(t), 2):
                arr.append(t[j] | t[j+1])
        else:
            for j in range(0, len(t), 2):
                arr.append(t[j] ^ t[j+1])
        count += 1
    return arr[0]


if __name__ == '__main__':
    [n, m] = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    for i in range(0, m):
        [p, d] = list(map(int, input().split(" ")))
        a[p-1] = d
        print(solve(a.copy()))
