def tell_sub_strings(s):
    sub_strings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            sub_strings.append(s[i:j])
    return sub_strings


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    count = 0
    if len(s1)<len(s2):
        sub_strings = tell_sub_strings(s1)
        for i in range(1, len(s2)+1):
            for j in range(len(s2)-i+1):
                tmp = s2[j:j+i]
                if tmp in sub_strings:
                    count += sub_strings.count(tmp)
    else:
        sub_strings = tell_sub_strings(s2)
        for i in range(1, len(s1)+1):
            for j in range(len(s1)-i+1):
                tmp = s1[j:j+i]
                if tmp in sub_strings:
                    count += sub_strings.count(tmp)
    print(count,end='')