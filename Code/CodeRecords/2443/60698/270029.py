def test():
    arr = list(eval(input()))
    used = [0] * len(arr)
    max=[0]
    m = findMax(arr, max, [], used)
    print(max[0])


def findMax(arr, max_num, arr_num, used):
    if len(arr_num) == len(arr):
        expr = ''
        for i in range(0, len(arr_num)):
            expr = expr + str(arr_num[i])
        if max_num[0] < int(expr):
            max_num[0] = int(expr)
    else:
        for i in range(0, len(arr)):
            if used[i] == 1:
                continue
            else:
                copy_arr_num = list(arr_num)
                copy_arr_num.append(arr[i])
                copy_used = list(used)
                copy_used[i] = 1
                findMax(arr, max_num, copy_arr_num, copy_used)

test()