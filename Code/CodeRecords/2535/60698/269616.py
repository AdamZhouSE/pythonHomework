def test():
    arr = eval(input())
    sorted_arr = sorted(arr)
    n = len(arr)
    seperated_arr = [[arr[i]] for i in range(0, len(arr))]
    result = seperate(seperated_arr, sorted_arr, n)
    print(result)


def seperate(seperated_arr, sorted_arr, n) -> int:
    for i in range(0, len(seperated_arr)):
        seperated_arr[i].sort()
    res = []
    for _ in range(0, len(seperated_arr)):
        res = res + seperated_arr[_]
    if res == sorted_arr:
        return n
    else:
        for i in range(0, len(seperated_arr) - 1):
            copy_s_arr = list(seperated_arr)
            copy_s_arr[i] = copy_s_arr[i] + copy_s_arr[i + 1]
            copy_s_arr.pop(i+1)
            return seperate(copy_s_arr,sorted_arr,n-1)

test()
