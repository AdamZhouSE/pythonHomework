a = list(input())
s = ''
if a[0] == '-':
    s = '-'
    a.pop(0)
a.reverse()
for i in a:
    if i == '0':
        a.remove(i)
print(s+''.join(a))




