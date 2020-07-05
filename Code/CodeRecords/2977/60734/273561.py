strings = []
for line in iter(input,'!'):
    strings.append(list(line.strip()))
res = []
for x in strings:
    for i in range(len(x)):
        if 'a'<=x[i]<='z':
            x[i] = chr(ord('z')-ord(x[i])+ord('a'))
        elif 'A'<=x[i]<='Z':
            x[i] = chr(ord('Z')-ord(x[i])+ord('A'))
    res.append(''.join(x))
print('\n'.join(res),end = '')

    