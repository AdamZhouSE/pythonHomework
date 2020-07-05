def most_seq():
    ls = eval(input())
    len_ls = len(ls)
    if len_ls == 0 or len_ls == 1:
        return len_ls
    start = end = 0
    max_len = 1
    while end < len_ls:
        if end == len_ls-1 or ls[end] >= ls[end+1]:
            temp = end - start + 1
            if temp > max_len:
                max_len = temp
            start = end = end + 1
        else:
            end += 1
    return max_len


print(most_seq())