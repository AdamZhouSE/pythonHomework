s = list(input())
t = list(input())
res = True
for i in s:
    if i in t:
        t.remove(i)
    else:
        res = False
        break
print(res)