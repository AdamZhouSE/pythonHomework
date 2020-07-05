def sum_char(string: str) -> int:
    res = 0
    for i in string:
        if i != ' ' and i != '\n':
            res += 1
    return res


s = input()
print(sum_char(s), end='')

