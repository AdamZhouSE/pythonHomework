import copy


def is_connect(ele, a_group):
    for mem in a_group:
        if ele[0] in a_group or ele[1] in a_group:
            return True
    return False


def form_group(a_group, relations_arr):
    added = 1
    while True:
        if added == 0:
            return
        added = 0
        for ele in copy.deepcopy(relations_arr):
            if is_connect(ele, a_group):
                relations_arr.remove(ele)
                a_group += ele
                added += 1


def divide(relations_arr, groups):
    while len(relations_arr) > 0:
        a_group = relations_arr[0]
        relations_arr.remove(relations_arr[0])
        form_group(a_group, relations_arr)
        a_group = list(set(a_group))
        groups.append(a_group)


def func():
    people_num, relations_num = input().split()
    people_num = int(people_num)
    relations_num = int(relations_num)
    price_arr = [int(x) for x in input().split()]
    relations_arr = []
    i = 0
    while i < relations_num:
        temp = [int(x) - 1 for x in input().split()]
        relations_arr.append(temp)
        i += 1

    groups = []
    divide(relations_arr, groups)
    all_people_in_groups = []

    i = 0
    while i < len(groups):
        j = 0
        while j < len(groups[i]):
            all_people_in_groups.append(groups[i][j])
            groups[i][j] = price_arr[groups[i][j]]
            j += 1
        i += 1

    min_gold = 0

    i = 0
    while i < len(price_arr):
        if i not in all_people_in_groups:
            min_gold += price_arr[i]
        i += 1

    for group in groups:
        min_gold += min(group)

    print(min_gold)


func()
