def min_str():
    lst = list(input())
    if ''.join(sorted(lst)) == 'achin':
        return ('achin')
    k = int(input())
    pre = ''.join(list(sorted(lst))[:k])
    while not ''.join(lst).startswith(pre):
        s_max = max(lst[:k])
        lst.remove(s_max)
        lst.append(s_max)
    return ''.join(lst)


print(min_str())
