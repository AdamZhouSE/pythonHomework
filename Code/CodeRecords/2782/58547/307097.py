def func():
    days = int(input())
    arr = []  # sale dollars records
    total = 0  # we will do summing while input
    i = 0
    while i < days:
        arr.append(int(input()))

        if i == 0:
            total += arr[0]
            i += 1
            continue

        min_val = 9999999
        j = 0
        while j < len(arr) - 1:
            if abs(arr[-1] - arr[j]) < min_val:
                min_val = abs(arr[-1] - arr[j])
            j += 1

        total += min_val

        i += 1

    print(total, end="", flush=True)


func()
