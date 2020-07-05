n = input().split(', ')
s = n[0][5:-1]
t = n[1][5:-1]

flag = False
for n in s:
    if n in t:
        flag = True
    else:
        flag = False
        break
if flag:
    print("true")
else:
    print("false")