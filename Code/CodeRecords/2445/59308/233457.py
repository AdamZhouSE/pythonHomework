s = input()
t = input()
flag = True
char_ = dict()
for i in range(len(s)):
    if s[i] in char_:
        a = char_.get(s[i])
        char_[s[i]] = a + 1
    else:
        char_[s[i]] = 1
for i in range(len(t)):
    if t[i] in char_:
        a = char_.get(t[i])
        if a == 0:
            flag = False
            break
        else:
            char_[t[i]] = a - 1
    else:
        flag = False
        break
if flag:
    print("true")
else:
    print("false")
