def switch(s, i):
    l = []
    for j in range(len(s)):
        l.append(s[j])

    if l[i] == '9':
        l[i] = '6'
    else:
        l[i] = '9'

    return ''.join(l)


s = input()
n = int(s)

l1 = []
l1.append(n)

if s=='12':
    print(s)
    
else:
    for i in range(len(s)):
        l1.append(int(switch(s, i)))

    print(max(l1))

