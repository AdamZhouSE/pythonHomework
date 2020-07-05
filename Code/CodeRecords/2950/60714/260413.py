s = input()
count2 = 0
count5 = 0
flag = True
for char in s:
    if char == '2':
        count2 += 1
    if char == '5':
        count5 += 1
    if count2 < count5:
        flag = False
        break
if not flag or count5 != count2:
    print(-1)
else:
    ans = 1
    is2 = False
    for char in s:
        if char == '2' and is2:
            ans += 1
        elif char == '2' and not is2:
            is2 = True
        else:
            is2 = False
    print(ans)
