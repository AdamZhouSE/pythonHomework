num = int(input())
for i in range(num):
    n, m = list(map(int, input().split(" ")))
    arr1 = list(map(int, input().split(" ")))
    arr = []
    for i in range(m, n * m + 1, m):
        arr.append(arr1[i - m:i])
    reverse = False
    while len(arr) != 0:
        if not reverse:
            first = arr.pop(0)
            print(" ".join(map(str, first)), end=" ")
            for j in range(len(arr) - 1):
                print(arr[j].pop(-1), end=" ")
        else:
            last = arr.pop(-1)
            print(" ".join(map(str, last[::-1])), end=" ")
            for j in range(len(arr)-1, 0, -1):
                print(arr[j].pop(0), end=" ")
        reverse = not reverse
    print()
