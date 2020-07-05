a = input()
b = input()
a = a[::-1]
b = b[::-1]
ci = 0
s = []
for i in range(max(len(a), len(b))):
    ai = int(a[i]) if len(a) > i else 0
    bi = int(b[i]) if len(b) > i else 0
    s.append(str(ai ^ bi ^ ci))
    ci = ai & bi | ai & ci | bi & ci
if ci == 1:
    s.append('1')

print(''.join(s[::-1]))
