def have_sub_sum_zero(arr, now_pos, is_chosen, bool_ref, now_val):
    if now_pos >= len(arr):
        return

    if bool_ref[0]:
        return

    if is_chosen:
        now_val += 1
    else:
        pass

    if now_val == 0:
        bool_ref[0] = True
        return

    have_sub_sum_zero(arr, now_pos + 1, True, bool_ref, now_val)
    have_sub_sum_zero(arr, now_pos + 1, False, bool_ref, now_val)


def func():
    test_num = int(input())
    i = 0
    bool_ref = [False]
    while i < test_num:
        input()  # eat
        arr = [[int(x), True] for x in input().split()]
        # number with a sign representing availability
        have_sub_sum_zero(arr, 0, True, bool_ref, 0)
        have_sub_sum_zero(arr, 0, False, bool_ref, 0)

        if bool_ref[0]:
            print("YES")
        else:
            print("NO")
            
        i += 1


func()
