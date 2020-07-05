delete = input()
s = []
t = input()
while t != "}":
    t = t.replace(delete.lower(), "")
    t = t.replace(delete.upper(), "")
    t = t.replace(" ", "")
    s.append(t)
    t = input()
s.append(t)
for x in s:
    print(x)
