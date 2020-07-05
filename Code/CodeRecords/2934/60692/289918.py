s = input()


def unfold(s1: str):
    if (s1.count('[') == 1) and (s1.count(']') == 1):
        s1 = s1[1:-1]
        d = int(s1[0])
        if '0' <= s1[1] <= '9':
            d = d * 10 + int(s1[1])
            return d * s1[2:]
        else:
            return d * s1[1:]
    mark = 0
    d = 0
    temp = ''
    s1 = s1[1:-1]
    for i in range(len(s1)):
        if '0' <= s1[i] <= '9':
            d = d * 10 + int(s1[i])
        else:
            mark = i
            break
    while mark < len(s1):
        if s1[mark] == '[':
            count = 1
            k = mark + 1
            while count:
                if s1[k] == '[':
                    count += 1
                if s1[k] == ']':
                    count -= 1
                k += 1
            temp += unfold(s1[mark:k])
            mark = k - 1
        else:
            temp += s1[mark]
        mark += 1
    return d * temp


i, j = 0, len(s) - 1
if not(s.count('[')) and not(s.count(']')):
    print(s,end="")
else:
    while s[i] != '[':
        i += 1
    while s[j] != ']':
        j -= 1
    if j == len(s) - 1:
        print(s[:i] + unfold(s[i:j + 1]),end="")
    else:
        print(s[:i] + unfold(s[i:j + 1]) + s[j + 1:],end="")
