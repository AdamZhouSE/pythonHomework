def main():
    list_1 = eval(input())
    list_2 = eval(input())
    sub_list_1 = sub_list(list_1)
    sub_list_2 = sub_list(list_2)
    if len(sub_list_1) > len(sub_list_2):
        maximum_overlaps(sub_list_2, sub_list_1)
    else:
        maximum_overlaps(sub_list_1, sub_list_2)


def sub_list(origin_list):
    result = [[]]
    for i in range(1, len(origin_list) + 1):
        temp_result = []
        for j in range(0, len(origin_list) - i + 1):
            temp_result.append(origin_list[j:j + i])
        result.append(temp_result)
    return result


def maximum_overlaps(list_1, list_2):
    result = 0
    for i in range(0, len(list_1)):
        sub_list_1 = list_1[len(list_1) - 1 - i]
        sub_list_2 = list_2[len(list_1) - 1 - i]
        for j in range(0, len(sub_list_1)):
            if sub_list_1[j] in sub_list_2:
                result = len(list_1) - 1 - i
                break
        if result != 0:
            break
    if result != 0:
        print(result)


if __name__ == "__main__":
    main()
