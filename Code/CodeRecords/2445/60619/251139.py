s = input()
t = input()
isSame = True
if len(s) != len(t):
    isSame = False
for i in s:
    if s.find(i) != t.find(i):
        isSame = False
        break
if isSame:
    print("true")
else:
    print("false")