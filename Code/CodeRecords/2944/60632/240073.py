n = list(input())
supp = []
for i in n:
    if i == '(':
        supp.append(i)
    elif i == ')':
        supp.pop()
    else:
        pass
if len(supp) == 0:
    print('YES',end='')
else:
    print('NO',end='')
