def change(p1, p2, p3, a, b):
    ans_l = []
    a_asc = ord(a)
    b_asc = ord(b)
    if a_asc >= b_asc:
        ans_l.append(a)
        ans_l.append('-')
        ans_l.append(b)
    elif a_asc + 1 == b_asc:
        ans_l.append(a)
        ans_l.append(b)
    elif (ord('0') <= a_asc <= ord('9') and ord('0') <= b_asc <= ord('9') and b_asc > a_asc + 1) or (
            ord('a') <= a_asc <= ord('z') and ord('a') <= b_asc <= ord('z') and b_asc > a_asc + 1):
        t = b_asc - a_asc - 1
        t_list = []
        for i in range(t):
            t_list.append(chr(a_asc + i + 1))
        if p3 == 2:
            t_list = t_list[::-1]
        tmp_list = []
        for i in range(t):
            for j in range(p2):
                tmp_list.append(t_list[i])
        ans_l.append(a)
        if p1 == 2 and ord('a') <= a_asc <= ord('z'):
            for i in tmp_list:
                ans_l.append(chr(ord('A') - ord('a') + ord(i)))
        elif p1 == 3:
            for i in range(len(tmp_list)):
                ans_l.append('*')
        else:
            for i in tmp_list:
                ans_l.append(i)
        ans_l.append(b)
    else:
        ans_l.append(a)
        ans_l.append('-')
        ans_l.append(b)
    ans_l.pop()
    return ans_l


p123 = [int(i) for i in input().split()]
p1 = p123[0]
p2 = p123[1]
p3 = p123[2]
s = input()
ans_list = []
for i in range(len(s)):
    ans_list.append(s[i])
    if s[i] == '-' and i < len(s) - 1:
        ans_list.pop()
        ans_list.pop()
        a = s[i - 1]
        b = s[i + 1]
        re = change(p1, p2, p3, a, b)
        for j in re:
            ans_list.append(j)
        i += 2
for i in ans_list:
    print(i, end='')
print()