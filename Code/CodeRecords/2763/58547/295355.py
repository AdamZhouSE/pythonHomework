def calc_seq_num(up_limit, max_seq_len):
    # A special sequence cannot exist if length
    # n is more than the maximum value m.
    if up_limit < max_seq_len:
        return 0

    # If n is 0, found an empty special sequence
    if max_seq_len == 0:
        return 1

    # There can be two possibilities : (1) Reduce
    # last element value (2) Consider last element
    # as m and reduce number of terms
    res = (calc_seq_num(up_limit - 1, max_seq_len) +
           calc_seq_num(up_limit // 2, max_seq_len - 1))
    return res


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        up_limit, max_seq_len = [int(x) for x in input().split()]
        print(calc_seq_num(up_limit, max_seq_len))
        i += 1


func()
