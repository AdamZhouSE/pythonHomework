if __name__ == '__main__':
    s1 = input()
    s2 = input()
    sub_strings = {}
    res = 0
    for i in range(1, len(s1)+1):
        for j in range(len(s1)-i+1):
            tmp = s1[j:j+i]
            if tmp in sub_strings.keys():
                sub_strings[tmp] += 1
            else:
                sub_strings[tmp] = 1
    for i in range(1, len(s2)+1):
        for j in range(len(s2)-i+1):
            tmp = s2[j:j+i]
            if tmp in sub_strings.keys():
                res += sub_strings[tmp]
    print(res, end='')