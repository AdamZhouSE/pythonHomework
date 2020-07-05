s=input()
t=input()

t2=''
for x in t:
    if x in s:
        t2+=x
if t2==s:
    print('True')
else:
    print('False')