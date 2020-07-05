oricode = input().strip()
leng = len(oricode)
li = [oricode+""]
for i in range(len(oricode)-1):
    t = oricode[leng-1]+oricode[0:leng-1]
    li.append(t+"")
    oricode = t
li = sorted(li)
res = ""
for i in li:
    res = res + i[leng-1]
print(res, end="")