def exchange(a, b, string):
    lst = list(string)
    sa = lst[int(a)]
    sb = lst[int(b)]
    lst[int(a)] = sb
    lst[int(b)] = sa
    string = ''.join(lst)
    return string


def combine(pair1, pair2,pairs):
    if pair1[0] == pair2[0]:
        if pair1[1] < pair2[1] :
            if pair1[1]+pair2[1] not in pairs:
                return pair1[1]+pair2[1]
        else:
            if pair2[1]+pair1[1] not in pairs:
                return pair2[1]+pair1[1]
    if pair1[1] == pair2[0]:
        if pair1[0] < pair2[1]:
            if pair1[0] + pair2[1] not in pairs:
                return pair1[0] + pair2[1]
        else:
            if pair2[1] + pair1[0] not in pairs:
                return pair2[1] + pair1[0]
    if pair1[0] == pair2[1]:
        if pair1[1] < pair2[0]:
            if pair1[1] + pair2[0] not in pairs:
                return pair1[1] + pair2[0]
        else:
            if pair2[0] + pair1[1] not in pairs:
                return pair2[0] + pair1[1]
    if pair1[1] == pair2[1]:
        if pair1[0] < pair2[0]:
            if pair1[0] + pair2[0] not in pairs:
                return pair1[0] + pair2[0]
        else:
            if pair2[0] + pair1[0] not in pairs:
                return pair2[0] + pair1[0]
    return ''


s = input()
pairs = ''.join(''.join(input().split(']')).split(','))[2:].split('[')

combined = True
while combined:
    combined = False
    l = len(pairs)
    for i in range(0, l):
        pair1 = pairs[i]
        for j in range(i + 1, len(pairs)):
            pair2 = pairs[j]
            if combine(pair1, pair2,pairs) != '':
                combined=True
                pairs.append(combine(pair1, pair2,pairs))

exchanged = True
while exchanged:
    exchanged = False
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        if s[int(a)] > s[int(b)]:
            s = exchange(a, b, s)
            exchanged=True
print(s)
