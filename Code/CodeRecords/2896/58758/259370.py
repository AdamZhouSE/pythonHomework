paper = [str(x) for x in input()]
letter = input()
flag = True
for ch in letter:
    if ch == ' ':
        continue
    else:
        try:
            ind = paper.index(ch)
            paper.pop(ind)
        except Exception:
            flag = False
            break
if flag:
    print('YES', end='')
else:
    print('NO', end='')
