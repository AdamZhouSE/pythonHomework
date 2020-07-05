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
        for sub_string in sub_strings:
            count += s2.count(sub_string)
    else:
        sub_strings = tell_sub_strings(s2)
        for sub_string in sub_strings:
            count += s1.count(sub_string)
    print(count,end='')