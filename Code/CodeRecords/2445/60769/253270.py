s = list(input())
t = list(input())
res = "true"
for i in s:
    if i in t:
        t.remove(i)
    else:
        res = "false"
        break
print(res)