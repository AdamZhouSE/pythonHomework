def good_substring(s, b, k):
    res = 0
    tmp = []
    for i in range(len(s)):
        sum = 1 - int(b[i])
        length = 1
        while sum <= k and length <= len(s)-i:
            if s[i:i+length] not in tmp:
                tmp.append(s[i:i+length])
                res += 1
            if length == len(s) - i:
                break
            sum += 1 - int(b[i+length])
            length += 1
    return res


if __name__ == '__main__':
    a = [input(), input(), eval(input())]
    result = good_substring(a[0], a[1], a[2])
    print(result)