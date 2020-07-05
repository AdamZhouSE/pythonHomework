def func(s:str, d:list) -> str:
    d.reverse()
    res = []
    maxlen = 0
    flag = 0
    d = sorted(d, key=lambda x: len(x))
    for item in d[::-1]:
        if flag == 1 and len(item) < maxlen:
            break
        i = j = 0
        while i < len(item) and j < len(s):
            if item[i] == s[j]:
                i += 1
            j += 1
        if i == len(item):
            flag = 1
            maxlen = len(item)
            res.append(item)
    if res == []:
        return ""
    elif len(res) == 1:
        return res[0]
    res.sort()
    return res[0]






string = input()
n = "l = " + input()
exec(n)
print(func(string,l))