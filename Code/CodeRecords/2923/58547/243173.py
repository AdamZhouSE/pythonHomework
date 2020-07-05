def sum_L_R(arr, field):
    total = 0
    i = field[0]
    while i <= field[1]:
        total += arr[i]
        i += 1
    return total


def func():
    temp_arr = [int(x) for x in input().split()]
    len_arr = temp_arr[0]
    queries_num = temp_arr[1]
    arr = [int(x) for x in input().split()]
    i = 0
    queries_frequency_pos = []
    # print(queries_frequency_pos)
    while i < len(arr):
        queries_frequency_pos.append([0, i])
        i += 1
    i = 0
    # print(queries_frequency_pos)
    L_R_s = []
    while i < queries_num:
        L, R = [int(x) - 1 for x in input().split()]
        L_R_s.append([L, R])
        j = L
        while j <= R:
            queries_frequency_pos[j][0] += 1
            j += 1
        i += 1

    # print(queries_frequency_pos)

    queries_frequency_pos.sort(reverse=True, key=lambda x: x[0])  # sort by value
    arr.sort(reverse=True)
    result_arr = [0] * len(arr)
    i = 0
    while i < len(arr):
        result_arr[queries_frequency_pos[i][1]] = arr[i]
        i += 1

    total = 0
    for L_R in L_R_s:
        total += sum_L_R(result_arr, L_R)

    print(total)


func()
