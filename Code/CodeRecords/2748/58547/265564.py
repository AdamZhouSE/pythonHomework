def del_redundant_bra(str_to_delete):
    if len(str_to_delete) < 2:
        return {''} if str_to_delete in '()' else {str_to_delete}

    res = set()
    for i in range(1, len(str_to_delete)):
        l = del_redundant_bra(str_to_delete[:i])
        r = del_redundant_bra(str_to_delete[i:])
        res |= {s1 + s2 for s1 in l for s2 in r}

    if str_to_delete[0] + str_to_delete[-1] == '()':
        res |= {'(' + ss + ')' for ss in del_redundant_bra(str_to_delete[1:-1])}
    max_len = max(len(ss) for ss in res)
    res = [ss for ss in res if len(ss) == max_len]
    return res


def func():
    str_to_delete = input()
    print(del_redundant_bra(str_to_delete))


func()
