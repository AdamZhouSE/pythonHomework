s = input()
t = input()
flag1 = False


if s[0] in t:
    flag1 = True

if flag1:
    for index in range(1, len(s)):
        if s[index] in t:
            flag1 = True
        else:
            flag1 = False
            break
    print(flag1)
else:
    print(flag1)