import re
t = input()
s = list([str(n) for n in re.findall(r"[a-z]+", input())])
s.sort(key=lambda x: (-len(x), x))
for word in s:
    cnt, flag = 0, True
    for ch in word:
        if ch not in t[cnt:]:
            flag = False
            break
        else:
            index = t[cnt:].index(ch) + cnt
            cnt = index + 1
    if flag:
        print(word)
        break