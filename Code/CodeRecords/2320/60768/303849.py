s = list(input())
k = int(input())
if k == 1:
    re = [''.join(s)]
    for i in range(len(s)):
        temp = s[0]
        s.pop(0)
        s.append(temp)
        re.append(''.join(s))
    re.sort()
    print(''.join(re[0]))
else:
    print(''.join(sorted(s)))