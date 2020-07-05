def test():
    n = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    count = 0
    neg = 0
    zero = 0
    for i in range(0, len(arr)):
        if arr[i] <= -1:
            count = count - 1 - arr[i]
            arr[i] = -1
            neg = neg + 1
        elif arr[i] >= 1:
            count = count + arr[i] - 1
            arr[i] = 1
        else:
            zero = zero + 1
    if zero != 0:
        count = count + zero
        print(count)
        return
    else:
        if neg % 2 != 0:
            count = count + 2
        print(count)


test()
