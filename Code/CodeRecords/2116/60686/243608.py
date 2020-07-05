n = int(input())
array_i = input().split(",")
for j in range(len(array_i)):
    array_i[j] = int(array_i[j])


def minimum(result, count, input_array):
    compare_list = []
    for k in range(len(input_array)):
        compare_list.append(result[count[k]] * input_array[k])
    minimal = compare_list[0]
    for m in range(len(compare_list)):
        if compare_list[m] < minimal:
            minimal = compare_list[m]
        else:
            continue
    return minimal


if n <= 1:
    print(n)
else:
    res = [1] * n
    i_count = [0] * len(array_i)
    i2 = i3 = i5 = 0
    for i in range(1, n):
        res[i] = minimum(res, i_count, array_i)
        while res[i] == res[i -1]:
            for x in range(len(i_count)):
                if res[i] == res[i_count[x]] * array_i[x]:
                    i_count[x] += 1
                    break
            res[i] = minimum(res, i_count, array_i)
        # res[i] = min(res[i2] * 2, min(res[i3] * 3, res[i5] * 5))
        for x in range(len(i_count)):
            if res[i] == res[i_count[x]] * array_i[x]:
                i_count[x] += 1
                break
print(res[-1])
