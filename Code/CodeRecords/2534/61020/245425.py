def get_parsed_int_list(s):
    integers = s[1:-1].split(",")

    b = 0
    while b < len(integers):
        integers[b] = int(integers[b])

        b += 1

    return integers


def get_merged_list(l1, l2):
    # 返回l1,l2归并后的列表

    result_list = []
    i, j = 0, 0

    while (i < len(l1)) and (j < len(l2)):
        if l1[i] <= l2[j]:
            result_list.append(l1[i])
            i += 1
        else:
            result_list.append(l2[j])
            j += 1

    if i == len(l1):
        result_list += l2[j:]
    else:
        result_list += l1[i:]

    return result_list


lists = input()[1:-1].split('],[')
# example imput:[[1,4,5],[1,3,4],[2,6]]


i = 0
while i < len(lists):
    if i == 0:
        lists[i] += ']'
    elif i == len(lists) - 1:
        lists[i] = '[' + lists[i]
    else:
        lists[i] = '[' + lists[i] + ']'

    lists[i] = get_parsed_int_list(lists[i])
    i += 1

result = lists[0]
for i_lst in lists[1:]:
    result = get_merged_list(result, i_lst)

print(result)
