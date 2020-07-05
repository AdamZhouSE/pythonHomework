import operator


def convert(arr_input):
    list_arr = []
    flag = True
    for j in range(len(arr_input)):
        list_arr.append(list(arr_input[j]))
        for x in range(len(list_arr[j])):
            if list_arr[j][x] == ' ':
                list_arr[j].pop(x)
                break
        list_arr[j].sort()
    result = [list_arr[0]]
    for y in range(len(list_arr)):
        for k in range(len(result)):
            if operator.eq(list_arr[y],result[k]):
                flag = False
        if flag:
            result.append(list_arr[y])
        flag = True
    return len(result)


nums = int(input())
arr = []
for i in range(nums):
    arr.append(input())
print(convert(arr), end = "")
