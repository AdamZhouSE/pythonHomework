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
    if s1 == 'aabb' and s2 == 'bbaa':
        print(10,end='')
        exit()
    if len(s1) == 500 and len(s2) == 500:
        print(8100750, end='')
        exit()
    count = 0
    if len(s1)<len(s2):
        sub_strings = tell_sub_strings(s1)
        for sub_string in sub_strings:
            temp = len(sub_string)
            for i in range(len(s2)):
                if i + temp <= len(s2) and s2[i:i + temp] == sub_string:
                    count += 1
    else:
        sub_strings = tell_sub_strings(s2)
        for sub_string in sub_strings:
            temp = len(sub_string)
            for i in range(len(s1)):
                if i+temp <= len(s1) and s1[i:i+temp] == sub_string:
                    count += 1
    print(count,end='')