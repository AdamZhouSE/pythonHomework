s=input()
t=input()
mark=0
for i in range(0,len(s)):
    if s[i] in t:
        continue
    else:
        mark=1
        break
if mark==1:
    print('False')
else:
    print('True')