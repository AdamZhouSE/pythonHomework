s = input()
t = input()
flag = False
for n in s:
    if n in t:
        flag = True
    else:
        flag = False
        break
print(flag)