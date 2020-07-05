# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。


def custom_sort(s):
    dictionary = {}
    res = ''
    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 1
        else:
            dictionary[s[i]] += 1
    for i in sorted(dictionary, key=dictionary.__getitem__, reverse=True):
        res += i * dictionary[i]
    return res


print(custom_sort(input()))