def solve():
    num = int(input())

    for _ in range(num):
        n, k = [int(i) for i in input().split(' ')]
        arr = [int(i) for i in input().split(' ')]

        res = calc(arr, n, k)
        print(res)


def calc(arr, n, k):
    dist_count = 0
    for i in range(n):

        j = 0
        while j < n:
            if (i != j and arr[j] == arr[i]):
                break
            j += 1

        if (j == n):
            dist_count += 1

        if (dist_count == k):
            return arr[i]

    return -1

solve()