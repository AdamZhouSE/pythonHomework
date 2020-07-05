from re import match
m, n = eval(input().replace(' ', ','))
A, B = input(), input()
# '[a\*]{1}[a-z][b\*]{1}'
pattern = ''
for ch in A:
    if ch != '*':
        pattern += '[' + ch + '\*]{1}'
    else:
        pattern += '[a-z]'
lst = []
for i in range(n - m + 1):
    if match(pattern, B[i:i + m]) is not None:
        lst.append(str(i + 1))
print(len(lst))
print(' '.join(lst) + ' ')
