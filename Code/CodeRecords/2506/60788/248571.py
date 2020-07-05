def f(s):
    if len(s) == 1:
        return 1
    s1 = s[0:int(len(s) / 2)]
    s2 = s[int(len(s) / 2):]
    length1 = f(s1)
    length2 = f(s2)
    length3 = 0
    if s1[len(s1) - 1] < s2[0]:
        s1.reverse()
        length3 = find_down(s1) + find_up(s2)

    return max(length1, length2, length3)


def find_down(s):
    length = 1
    if len(s) == 1:
        return length
    for i in range(0, len(s) - 1):
        if s[i + 1] < s[i]:
            length += 1
        else:
            return length
    return length


def find_up(s):
    length = 1
    if len(s) == 1:
        return length
    for i in range(0, len(s) - 1):
        if s[i + 1] > s[i]:
            length += 1
        else:
            return length
    return length


s = [int(x) for x in input().split(',')]
print(f(s))
