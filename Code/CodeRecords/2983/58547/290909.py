def func():
    str_len = int(input())
    str_list = list(input())

    # n为奇数时，如果已经有一个字符出现的次数为奇数，还找到了一个字符出现的次数为奇数，那么就不能构成回文串；
    # n为偶数时，只要找到有一个字符出现的次数为奇数，那么就不能构成回文串。
    sl_set = list(set(str_list))
    sl_dict = {ele: 0 for ele in sl_set}

    for ele in str_list:
        sl_dict[ele] = (sl_dict[ele] + 1) % 2

    if str_len % 2 == 0 and 1 in sl_dict.values():
        print("Impossible")
        return

    if str_len % 2 == 1 and list(sl_dict.values()).count(1) > 1:
        print("Impossible")
        return

    steps = 0
    if str_len % 2 == 0:
        # even number cases
        i = 0
        while i < str_len // 2:
            now_char = str_list[i]
            find_cur = str_len - 1 - i
            while True:
                if str_list[find_cur] == now_char:
                    steps += str_len - 1 - i - find_cur
                    str_list.pop(find_cur)
                    str_list.insert(str_len - 1 - i, now_char)
                    break
                find_cur -= 1
            i += 1
    else:
        # odd number cases
        # this case the center odd-time number will be adjusted automatically
        the_char = ''
        for ele in sl_dict.keys():
            if sl_dict[ele] == 1:
                the_char = ele
                break
        i = 0
        while i < str_len // 2:
            now_char = str_list[i]
            find_cur = str_len - 1 - i
            while True:
                # will definitely be found, so while True is fine
                if str_list[find_cur] == now_char:
                    steps += str_len - 1 - i - find_cur
                    str_list.pop(find_cur)
                    str_list.insert(str_len - 1 - i, now_char)
                    break
                find_cur -= 1
            i += 1

    # print(str_list)
    print(steps)


func()
