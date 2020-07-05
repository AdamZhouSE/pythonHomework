arrs = eval(input())
arr_res = list(arrs[0])
for arr in arrs[1:]:
    index, i = 0, 0
    while i < len(arr):
        if index >= len(arr_res):
            arr_res.extend(arr[i:])
            break
        elif arr[i] < arr_res[index]:
            arr_res.insert(index, arr[i])
            i += 1
        index += 1

print(arr_res)
