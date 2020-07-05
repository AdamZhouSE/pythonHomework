s = input()
t = input()
res = True
temp = 0
for i in s:
    if not t.count(i):
        res = False
        break
    else:
        if t.index(i) < temp:
            res = False
            break
        else:
            temp = t.index(i)
print(res)