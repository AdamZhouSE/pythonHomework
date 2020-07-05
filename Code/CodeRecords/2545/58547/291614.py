def have_sub_sum_zero(arr, now_pos, is_chosen, bool_ref, now_val, had_added):
    if bool_ref[0]:
        return

    if is_chosen:
        now_val += arr[now_pos]
        had_added = True
    else:
        pass

    if now_val == 0 and had_added:
        bool_ref[0] = True
        return

    if now_pos == len(arr) - 1:
        return

    have_sub_sum_zero(arr, now_pos + 1, True, bool_ref, now_val, had_added)
    have_sub_sum_zero(arr, now_pos + 1, False, bool_ref, now_val, had_added)


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        bool_ref = [False]
        input()  # eat
        arr = [int(x) for x in input().split()]

        have_sub_sum_zero(arr, 0, True, bool_ref, 0, False)
        have_sub_sum_zero(arr, 0, False, bool_ref, 0, False)

        if bool_ref[0]:
            print("Yes")
        else:
            print("No")

        i += 1


func()
