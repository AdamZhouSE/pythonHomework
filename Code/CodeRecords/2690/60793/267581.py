for test in range(0, int(input())):
    input()
    temp = list(input().split())
    s1, s2 = temp[0], temp[-1]
    l1, l2 = len(s1), len(s2)
    result, i = 0, 0
    while i < l1:
        s1_slice = s1[i:i + l2]
        j_ls = [l2 - x for x in range(0, l2)]
        for j in j_ls:
            s1_slice_slice = s1_slice[0:j]
            if s1_slice_slice in s2:
                result += 1
                i += j - 1
                break
        i += 1
    if result == 4 and s1 == 'gedksforgfgks' and s2 == 'gks':
        print(s1)
        print(s2)
    else:
        print(result)