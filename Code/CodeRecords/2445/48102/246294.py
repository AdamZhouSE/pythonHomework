import re


def judge(s_ls: list, t_ls: list) -> bool:
    if len(s) != len(t):
        return False
    s_ls.sort()
    t_ls.sort()
    for i in range(len(s_ls)):
        if s_ls[i] != t_ls[i]:
            return False
    return True


string = input()
match_obj = re.match(r's = "(.*)", t = "(.*)"', string)
s = list(match_obj.group(1))
t = list(match_obj.group(2))
if judge(s, t):
    print('true')
else:
    print('false')