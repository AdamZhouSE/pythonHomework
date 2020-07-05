def min_str():
    string = input()
    lst = list(string)
    k = int(input())
    if k >= 2:
        return ''.join(sorted(lst))
    idx = string.index(min(string))
    return string[idx:] + string[:idx]


print(min_str())
