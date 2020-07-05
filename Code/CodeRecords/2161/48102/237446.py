def str_multi():
    a = input()
    b = input()
    if a == '0' or b == '0':
        return 0
    len_a = len(a)
    len_b = len(b)
    ls = []
    string = ''
    for i in range(len_b-1, -1, -1):
        i_bit = int(b[i])
        com = len_b - i - 1
        carry = 0
        res = []
        for j in range(len_a-1, -1, -1):
            j_bit = int(a[j])
            muti = i_bit * j_bit
            res.insert(0, muti % 10 + carry)
            carry = i_bit * j_bit // 10
        if carry == 1:
            res.insert(0, 1)
        for k in range(com):
            res.append(0)
        ls = sum_str(ls, res)
    ls = list(map(str, ls))
    return ''.join(ls)


def sum_str(ls, res):
    len_ls = len(ls)
    len_res = len(res)
    sum_ls = []
    if len_ls == 0:
        ls = res
        return ls
    else:
        carry = 0
        for i in range(max(len_ls, len_res)):
            index_a = len_ls - 1 - i
            index_b = len_res - 1 - i
            a = ls[len_ls-1-i] if index_a >= 0 else 0
            b = res[len_res-1-i] if index_b >= 0 else 0
            suming = a + b
            sum_ls.insert(0, suming % 10 + carry)
            carry = suming // 10
        if carry == 1:
            sum_ls.insert(0, 1)
        ls = sum_ls
        return ls


print(str_multi())