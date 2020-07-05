t = int(input())
ans_l = []
for i in range(t):
    s = input()
    patt = input()
    patt_l = []
    for j in range(len(patt)):
        patt_l.append(patt[j])
    is_get = False
    for j in range(len(s)):
        if s[j] in patt_l:
            ans_l.append(s[j])
            is_get = True
            break
    if not is_get:
        ans_l.append('$')
for i in ans_l:
    print(i)
