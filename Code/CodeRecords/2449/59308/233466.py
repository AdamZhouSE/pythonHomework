import re
title = input()
pattern = re.compile('\\"[a-z]*\\"')
result = pattern.findall(title)

s = result[0]
t = result[1]

flag = True
char_ = dict()
for i in range(len(s)):
    if s[i] in char_:
        a = char_[s[i]]
        char_[s[i]] = a + 1
    else:
        char_[s[i]] = 1
for i in range(len(t)):
    if t[i] in char_:
        a = char_[t[i]]
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
