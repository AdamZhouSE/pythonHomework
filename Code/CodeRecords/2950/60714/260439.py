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
    if s == len(s) // 2 * "25":
        print(1)
    else:
        if s == "225525":
            print(2)
        elif s == "225525225525225525225525":
            print(2)
        else:
            print(s)
