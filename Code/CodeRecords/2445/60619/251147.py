li = input().split(",")
s = li[0].strip().replace("\"", "").replace(" ", "")[2:]
t = li[1].strip().replace("\"", "").replace(" ", "")[2:]
isSame = True
if len(s) != len(t):
    isSame = False
for i in s:
    if s.count(i) != t.count(i):
        isSame = False
        break
if isSame:
    print("true")
else:
    print("false")