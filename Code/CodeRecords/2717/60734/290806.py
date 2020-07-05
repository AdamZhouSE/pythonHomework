def find(x):
    if  x!= variables[x]:
        variables[x] = find(variables[x])
    return variables[x]

import re
eqs = re.findall(r'"(.*?)"', input())
variables = {chr(i):chr(i) for i in range(97,125)}
flag = True
for eq in eqs:
    if eq[1] == '=':
        variables[find(eq[0])] = find(eq[-1])
    else:
        if find(eq[0]) == find(eq[-1]):
            flag = False
            break
if flag:
    print('true')
else:
    print('false')