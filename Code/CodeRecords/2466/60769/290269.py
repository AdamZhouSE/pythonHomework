def solve(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] > arr[k]:
                    count += 1
    print(count)


if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        n = int(input())
        arr = sorted(map(int, input().split()))
        solve(arr)
