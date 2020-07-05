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
    sub_string1 = tell_sub_strings(s1)
    sub_string2 = tell_sub_strings(s2)
    count = 0
    for sub_string in sub_string1:
        if sub_string2.__contains__(sub_string):
            count += sub_string2.count(sub_string)
    print(count,end='')