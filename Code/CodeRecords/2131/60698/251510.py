def test():
    a = input()
    arr = a.split(',')
    arr = list(map(int, arr))
    sum = []
    for j in range(0, len(arr)):
        sum.append(0)
    if len(arr) <= 2:
        print(0)
        return
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] == arr[i - 1] - arr[i - 2]:
            sum[i] = sum[i - 1] + 1
    result = 0
    for k in range(0, len(sum)):
        result = sum[k] + result
    print(result)


test()