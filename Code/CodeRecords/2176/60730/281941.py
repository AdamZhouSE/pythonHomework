s = list(input())
s.__reversed__()
m = []
for i in range(len(s)):
    if (len(s) - i) in m:
        continue

    if i == len(s) - 1:
        if 1 not in m:
            print(1, end='')
        break
    for j in range(i + 1, len(s)):
        if len(m) == len(s) - 1:
            if (len(s) - j) not in m:
                print(len(s) - j, end='')
                m.append(len(s) - j)
        if s[i] > s[j]:
            if (len(s) - j) not in m:
                print(len(s) - j, end=' ')
                m.append(len(s) - j)

    if len(m) == len(s) - 1:
        if (len(s) - i) not in m:
            print(len(s) - i, end='')
            m.append(len(s) - i)
    else:
        print(len(s) - i, end=' ')
        m.append(len(s) - i)
print()