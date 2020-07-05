def is_next(a, b):
    now_ele = list(sorted(a))
    next_ele = list(sorted(b))
    count = 0
    i = 0
    j = 0
    while i < len(now_ele):
        if now_ele[i] != next_ele[j]:
            count += 1
            if count > 1:
                return False
            j += 1
            continue
        i += 1
        j += 1

    if j == len(next_ele) - 1:
        count += 1

    if count == 1:
        return True
    else:
        return False


def func():
    lib = []
    try:
        while True:
            now = list(input())
            lib.append(now)
            # sort
    except EOFError:
        pass

    lib.sort(key=lambda x: len(x))
    # sort ny length

    max_word_len = len(lib[-1])
    min_word_len = len(lib[0])

    dict_len_strslists = {}
    i = 0
    now_len = min_word_len - 1
    while i < len(lib):
        if len(lib[i]) != now_len:
            now_len += 1
            dict_len_strslists[now_len] = [lib[i]]
        else:
            dict_len_strslists[now_len].append(lib[i])
        i += 1

    max_res = 1
    max_pos = [0, 0]
    dp = [[1 for y in range(0, len(dict_len_strslists[x]))] for x in range(min_word_len, max_word_len + 1)]
    father = [[[-1, -1] for y in range(0, len(dict_len_strslists[x]))] for x in range(min_word_len, max_word_len + 1)]
    i = 1
    while i < max_word_len - min_word_len + 1:
        j = 0
        while j < len(dict_len_strslists[i + min_word_len]):
            k = 0
            while k < len(dict_len_strslists[i + min_word_len - 1]):
                if is_next(dict_len_strslists[i + min_word_len - 1][k], dict_len_strslists[i + min_word_len][j]):
                    if dp[i - 1][k] + 1 > dp[i][j]:
                        dp[i][j] = dp[i - 1][k] + 1
                        father[i][j] = [i - 1, k]
                k += 1
            if dp[i][j] > max_res:
                max_res = dp[i][j]
                max_pos = [i, j]
            j += 1
        i += 1

    res_seq = []
    now = max_pos
    while now != [-1 ,-1]:
        res_seq.insert(0, "".join(dict_len_strslists[now[0] + min_word_len][now[1]]))
        now = father[now[0]][now[1]]

    print(max_res)
    for ele in res_seq:
        print(ele)


func()
