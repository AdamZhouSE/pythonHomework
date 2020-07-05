s = input()
t = input()
if s == '':
    print(True)
loc = -1
for i in s:
    loc = t.find(i, loc + 1)
    if loc == -1:
        break
if loc == -1:
    print(False)
else:
    print(True)
