s = input()
fre = {}
for x in s:
    fre[x] = fre[x] + 1 if x in fre else 1

s = [(k, fre[k]) for k in s]
s.sort(reverse=True, key=lambda x: x[1])
print(''.join([k for k, v in s]))
