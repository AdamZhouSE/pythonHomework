s = input()
s1 = ""
for i in s:
    if i == "-":
        continue
    s1 = i + s1
    s1 = s1.lstrip("0")
if "-" in s:
    s1 = "-" + s1
print(s1)
