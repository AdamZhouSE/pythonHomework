flag = 0
s = input()
for i in range(len(s)):
    a = s[i]
    if i == 0 and a == ')':
        print('NO', end='')
        break
    if a == "(":
        flag = flag + 1
    if a == ")":
        flag = flag - 1
    if flag < 0:
        print("NO", end='')
        break
    if a == "@":
        if flag == 0:
            print("YES", end='')
        else:
            print("NO", end='')
