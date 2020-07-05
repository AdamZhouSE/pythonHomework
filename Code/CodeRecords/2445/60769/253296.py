s, t = input().rstrip("\"").lstrip("s = \"").split("\", t = \"")
s = list(s)
t = list(t)
res = "true"
for i in s:
    if i in t:
        t.remove(i)
    else:
        res = "false"
        break
print(res)
