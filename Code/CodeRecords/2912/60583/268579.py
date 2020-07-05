def no_repeat_str(s):
    res_list = []
    length = len(s)
    for i in range(length):
        tmp = s[i]
        for j in range(i + 1, length):
            if s[j] not in tmp:
                tmp += s[j]  
            else:
                break
        res_list.append(tmp)
    for i in range(len(res_list)):
        k = i
        j = i + 1
        while j < len(res_list):
            if len(res_list[k]) > len(res_list[j]):
                k = j
            j += 1
        if i != k:
            res_list[i], res_list[k] = res_list[k], res_list[i]
    return res_list[-1]
if __name__ == '__main__':
    str_list = ['abcabcbb']
    for s in str_list:
        res = no_repeat_str(s)
    print('%s' % len(res))
