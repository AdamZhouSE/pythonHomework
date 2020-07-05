t=eval(input())
t = sorted(t)
for i in range(len(t)):
    if t[i].split(':')[0].startswith('0'):
        a = t[i].split(':')[0].lstrip('0')
        if not a :
            t.append('24:' + t[i].split(':')[1])
        else:
            t.append(str(24 + int(a)) + ':' + t[i].split(':')[1])
    else:
        break
ans = 99999999
for i in range(len(t) - 1):
    h1 = int(t[i].split(':')[0].lstrip('0')) if t[i].split(':')[0] != '00' else 0
    m1 = int(t[i].split(':')[1]) if t[i].split(':')[1] != '00' else 0
    h2 = int(t[i + 1].split(':')[0].lstrip('0')) if t[i + 1].split(':')[0] != '00' else 0
    m2 = int(t[i + 1].split(':')[1]) if t[i + 1].split(':')[1] != '00' else 0
    ans = min(ans, (h2 - h1) * 60 + (m2 - m1))
print(ans)
