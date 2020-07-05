def address(s):
    like = []
    i = 0
    while i < len(s):
        if s[i] == '[' or s[i] == ',' or s[i] == ']':
            i = i + 1
            continue
        like.append(s[i])
        i = i + 1
    i = 0
    while i < len(like):
        like[i] = int(like[i])
        i = i + 1
    return like


def sort(s):
    i = 1
    j = 0
    leng = len(s)
    for i in range(1, leng):
        for j in range(0, i):
            if s[i] < s[j]:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp

    return s


a = input()
print(sort(address(a)))
