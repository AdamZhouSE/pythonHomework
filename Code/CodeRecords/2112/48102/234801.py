def find_num():
    num_ls = input().split(',')
    num_ls = list(map(int, num_ls))
    len_num = len(num_ls)
    res = (len_num + 1) * len_num // 2 - sum(num_ls)
    print(res)
    return


find_num()
