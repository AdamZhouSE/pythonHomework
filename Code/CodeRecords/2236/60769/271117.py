n = int(input())
arr = []
for i in range(n):
    opt, x = list(map(int, input().split()))
    if opt == 1:
        arr.append(x)
        arr = sorted(arr)
    elif opt == 3:
        arr.remove(x)
        print(x)
    elif opt == 4:
        print(arr[x - 1])
    elif opt == 5:
        arr.append(x)
        arr = sorted(arr)
        print(arr[arr.index(x) - 1])
        arr.remove(x)
    elif opt == 6:
        arr.append(x)
        arr = sorted(arr)
        index = arr.index(x)
        while arr[index] == x:
            index += 1
        print(arr[index])
        arr.remove(x)
