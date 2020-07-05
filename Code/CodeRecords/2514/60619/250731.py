s = input()
t = input()
start = 0
isSon = True
for i in range(len(s)):
    index = t.find(s[i], start)
    if index != -1:
        start = index
    else:
        isSon = False
        break
print(isSon)