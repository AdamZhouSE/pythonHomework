s=input()
t=input()
sign=1
for i in range(len(s)):
    if t.count(s[i])==0:
        sign=0
        break
    else:
        t=t[t.index(s[i])+1:]
if sign==1:
    print('True')
else:
    print('False')
    