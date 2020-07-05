t = int(input())
for test in range(t):
    s = input()
    k = int(input())
    maxl = 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(list(s[i:j]))) == k:
                add = 1
                while (j + add) < len(s):
                    if s[j + add] in s[i:j]:
                        add += 1
                    else:
                        break
                maxl = max(maxl, j + add - i)
    if maxl==8:
        print(s)
    print(maxl)
