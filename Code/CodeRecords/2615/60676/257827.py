def method(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        if ord(s[0]) < ord(s[1]):
            return s[::-1]
        else:
            return s
    start = 0
    dif = ord(s[1]) - ord(s[0])
    res = ''
    for i in range(2, len(s)):
        if ord(s[i]) - ord(s[i-1]) != dif or (i == len(s) - 1 and ord(s[i]) - ord(s[i-1]) == dif):
            tmp = s[start:i]
            if ord(s[i]) - ord(s[i-1]) == dif:
                tmp = s[start:]
            if len(tmp) > 1 and ord(tmp[0]) < ord(tmp[1]):
                tmp = tmp[::-1]
            if len(tmp) > len(res):
                res = tmp
            elif len(tmp) == len(res):
                if ord(tmp[0]) > ord(res[0]):
                    res = tmp
            dif = ord(s[i]) - ord(s[i-1])
            start = i - 1
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        result.append(method(input()))
    for i in range(len(result)):
        print(result[i])