def del_word(string: str, ls: list) -> str:
    res = ''
    for i in ls:
        if judge(string, i):
            if len(i) > len(res):
                res = i
            elif len(i) == len(res):
                if i < res:
                    res = i
    return res


def judge(string: str, r: str) -> bool:
    if r == '':
        return True
    if r[0] not in string:
        return False
    else:
        idx = string.index(r[0])
        return True and judge(string[idx+1:], r[1:])


s = input()
lst = eval(input())
print(del_word(s, lst))