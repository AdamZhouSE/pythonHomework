s = input()


def unfold(s1: str):
    d = 0
    if (s1.count('[') == 0) and (s1.count(']') == 0):
        d = int(s1[0])
        if '1' <= s1[1] <= '9':
            d = d * 10 + int(s1[1])
            return d * s1[2:]
        else:
            return d * s1[1:]
    i, j = 0, len(s1) - 1
    while s1[i] != '[':
        i += 1
    while s1[j] != ']':
        j -= 1
    d = int(s[:i])
    if j == len(s1) - 1:
        return d * unfold(s1[i + 1:j])
    else:
        return d * (unfold(s[i + 1:j]) + s1[j + 1:])



i, j = 0, len(s) - 1
if not(s.count('[')) and not(s.count(']')):
    print(s)
else:
    while s[i] != '[':
        i += 1
    while s[j] != ']':
        j -= 1
    if j == len(s) - 1:
        print(s[:i] + unfold(s[i + 1:j]))
    else:
        print(s[:i] + unfold(s[i + 1:j]) + s[j + 1:])