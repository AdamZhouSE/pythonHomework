def find(x):
    if x != tmp[x]:
        tmp[x] = find(tmp[x])
    return tmp[x]

s=input()
s=s[2:len(s)-2].split('","')
tmp = {chr(i): chr(i) for i in range(97, 125)}
for it in s:
    if it[1] == '=':
        tmp[find(it[0])] = find(it[-1])

flag="true"
for it in s:
    if it[1] == '!':
        if find(it[0]) == find(it[-1]):
            flag="false"
print(flag)