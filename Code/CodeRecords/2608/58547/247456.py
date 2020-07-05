vowels_const = list("aeiou")
consonants_const = list("bcdfghjklmnpqrstvwxyz")


def print_strings(cursor, is_chosen, string_in_list, string_now_ref, res):
    if cursor >= len(string_in_list):
        if len(string_now_ref) < 2 or \
                string_now_ref[0] not in vowels_const \
                or string_now_ref[-1] not in consonants_const:
            return
        if string_now_ref not in res:
            res.append(string_now_ref)
        return
    if not is_chosen:
        print_strings(cursor + 1, True, string_in_list, string_now_ref, res)
        print_strings(cursor + 1, False, string_in_list, string_now_ref, res)
    else:  # is chosen
        if len(string_now_ref) != 0 and string_now_ref[0] in vowels_const:
            string_now_ref += string_in_list[cursor]
        else:
            if string_in_list[cursor] in vowels_const:
                string_now_ref += string_in_list[cursor]
        print_strings(cursor + 1, True, string_in_list, string_now_ref, res)
        print_strings(cursor + 1, False, string_in_list, string_now_ref, res)


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        string_in = list(input())
        flag = False

        if not flag and len(string_in) == 0:
            print(-1)
            i += 1
            flag = True
            break

        while not flag and string_in[0] not in vowels_const:
            string_in.pop(0)
            if len(string_in) == 0:
                print(-1)
                i += 1
                flag = True
                break

        if not flag and len(string_in) == 0:
            print(-1)
            i += 1
            flag = True
            break

        while not flag and string_in[-1] not in consonants_const:
            string_in.pop(-1)
            if len(string_in) == 0:
                print(-1)
                i += 1
                flag = True
                break

        if not flag and len(string_in) == 0:
            print(-1)
            i += 1
            flag = True
            break

        if flag:
            continue

        res = []

        print_strings(0, True, string_in, "", res)
        print_strings(0, False, string_in, "", res)

        res.sort()

        j = 0
        while j < len(res):
            print(res[j], end="", flush=True)
            if j != len(res) - 1:
                print(" ", end="", flush=True)
            j += 1
        print()

        i += 1


func()
