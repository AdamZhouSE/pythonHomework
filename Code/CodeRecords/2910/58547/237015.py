def func():
    n = int(input())
    arr = []
    i = 0
    while i < n:
        temp = [int(x) for x in input().split(" ")]
        arr.append(temp[:])
        i += 1

    sequence = []
    i = 0
    while i < n:
        if i == 0:
            sequence.append(max(arr[0]))
            i += 1
            continue
        if min(arr[i]) <= sequence[i-1]:
            sequence.append(min(arr[i]))
        elif max(arr[i]) <= sequence[i-1]:
            sequence.append(max(arr[i]))
        else:
            print("NO")
            return
        i += 1

    print("YES")


func()
