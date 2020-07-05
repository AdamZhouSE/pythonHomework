def func():
    n = int(input())
    arr = []
    i = 0
    while i < n:
        temp = [int(x) for x in input().split(" ")]
        arr.append(temp)
        i += 1

    pairs = 0
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if arr[i][0] in arr[j] or arr[i][1] in arr[j]:
                pairs += 1
            j += 1
        i += 1
    if pairs == 12:
        print(arr)
    print(pairs)


func()
