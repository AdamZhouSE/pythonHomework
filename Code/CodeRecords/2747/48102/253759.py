def one_diff(s1: str, s2: str) -> bool:
    count = 0
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


def find(start: str, end: str, dic: list) -> list:
    if end not in dic:
        return []
    res = []
    count = 2**31-1

    def dfs(s: str, e: str, d: list, temp: list):
        nonlocal res
        nonlocal count
        if s == e:
            if len(temp) < count:
                res = [temp.copy()]
                count = len(temp)
            elif len(temp) == count:
                res.append(temp.copy())
            return
        for i in d:
            if one_diff(s, i):
                temp.append(i)
                lst = d.copy()
                lst.remove(i)
                dfs(i, e, lst, temp)
                temp.remove(i)

    dfs(start, end, dic, [start])
    return res


string_1 = input()
string_2 = input()
ls = eval(input())
print(find(string_1, string_2, ls))