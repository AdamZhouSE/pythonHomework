def make_child_list(number_list, arr, cursor, is_chosen, now_number_str):
    if cursor >= len(number_list):
        if len(now_number_str) != 0 and int(now_number_str) not in arr:
            arr.append(int(now_number_str))
        return
    if not is_chosen:
        make_child_list(number_list, arr, cursor + 1, True, now_number_str)
        make_child_list(number_list, arr, cursor + 1, False, now_number_str)
    else:
        make_child_list(number_list, arr, cursor + 1, True, now_number_str + number_list[cursor])
        make_child_list(number_list, arr, cursor + 1, False, now_number_str + number_list[cursor])


def all_child(number):
    number_list = list(str(number))
    arr = []
    make_child_list(number_list, arr, 0, True, "")
    make_child_list(number_list, arr, 0, False, "")
    return arr


def number_product(all_child_list):
    products = []
    i = 0
    while i < len(all_child_list):
        str_now = str(all_child_list[i])
        product_now = 1
        j = 0
        while j < len(str_now):
            product_now *= int(str_now[j])
            j += 1
        products.append(product_now)
        i += 1
    return products


def is_lucky(number):
    all_child_list = all_child(number)
    number_product_list = number_product(all_child_list)
    if len(number_product_list) == len(set(number_product_list)):
        return True
    else:
        return False


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        number = int(input())
        if is_lucky(number):
            print("1")
        else:
            print("0")
        i += 1


func()
