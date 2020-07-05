s = input()
t = input()
start = 0
flag = True
for ch in s:
    try:
        ind = t.index(ch, start)
        start = ind + 1
    except Exception:
        flag = False
        break
print(flag)
