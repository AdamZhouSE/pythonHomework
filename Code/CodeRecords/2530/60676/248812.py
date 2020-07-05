def custom_sort(dic, s):
    res = ''
    for i in range(len(dic)):
        j = 0
        while j < (len(s)):
            if dic[i] == s[j]:
                res += s[j]
                s = s[:j] + s[j+1:]
            j += 1
    res += s
    return res


print(custom_sort(input(), input()))