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

    # 如果 n 为偶数，那么从第一字符开始，从后往前找第一个和它相同的字符，如果找了，就将找到的字符交换到最后一个位置，在下一次遍历时，
    # 就可以不用管刚才已经交换好的那来两个字符；下一次从第二个字符开始，从倒数第二个字符开始遍历，执行和上述相同的操作；
    # 如果 n 为奇数，在字符串的某一个位置找到了那个出现次数为奇数的字符，我们不必将次字符现在就交换到中间位置，
    # 而是先计算它到中间位置需要交换的次数，然后累加到 cnt 中，将剩下的字符都交换到对称后，再交换这个字符即可。
    # 试着想一想，如果第一个字符就为出现次数为奇数的字符，那么将它交换到中间位置，接下来交换其他字符时，每次的交换次数都会多一次。
    # 这其实是一种普遍的规律。

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
