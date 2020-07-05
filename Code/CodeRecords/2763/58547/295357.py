def calc_seq_num(up_limit, max_seq_len):
    if up_limit < max_seq_len:
        return 0

    if max_seq_len == 0:
        return 1

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
