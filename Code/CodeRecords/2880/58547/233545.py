def func():
    tArr = input()
    tArr = [int(n) for n in tArr.split(" ")]
    n = int(tArr[0])  # 人数
    k = int(tArr[1])  # 体重界限
    arr = input()
    arr = [int(n) for n in arr.split(" ")]

    outKids = 0

    i = 0
    while i < n:
        if arr[i] <= k:
            outKids += 1
        else:
            break
        i += 1

    if i == n:
        print(outKids)
        return 

    i = n - 1
    while i > -1:
        if arr[i] <= k:
            outKids += 1
        else:
            break
        i -= 1

    print(outKids)

func()
