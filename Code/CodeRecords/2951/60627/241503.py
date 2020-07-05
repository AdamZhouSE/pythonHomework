# 14
b2 = input()
b3 = input()
def f2(s):
    t = 0
    for i in range(len(s)):
        t += int(s[len(s)-i-1])*(2**i)
    return t
def f3(s):
    t = 0
    for i in range(len(s)):
        t += int(s[len(s)-i-1])*(3**i)
    return t
b2_l = []
for i in range(len(b2)):
    sub = b2[:]
    c = '1' if sub[i] =='0' else '0'
    sub = sub[:i]  +c + sub[i+1:]
    b2_l.append(f2(sub))
b3_l = []
for i in range(len(b3)):
    sub = b3[:]
    if sub[i] == '0':
        c = '1'
    elif sub[i] == '1':
        c = '2'
    else:
        c = '0'
    sub = sub[:i]  +c + sub[i+1:]
    b3_l.append(f3(sub))
for i in range(len(b3)):
    sub = b3[:]
    if sub[i] == '0':
        c = '2'
    elif sub[i] == '1':
        c = '0'
    else:
        c = '1'
    sub = sub[:i]  +c + sub[i+1:]
    b3_l.append(f3(sub))
for i in b3_l:
    if i in b2_l:
        print(i,end = '')
        break