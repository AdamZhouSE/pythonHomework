def judge(string: str, target: str) -> bool:
    table = {}
    s = set(string)
    for i in s:
        if i != ' ':
            table[i] = string.count(i)
    for i in target:
        if i not in s:
            return False
        else:
            if i != ' ':
                if table[i] != 0:
                    table[i] -= 1
                else:
                    return False
    return True


s1 = input()
s2 = input()
if judge(s1, s2):
    print('YES', end='')
else:
    print('NO', end='')