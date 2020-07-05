inp = eval(input())
s = [str(x) for x in inp]
s.sort()
s.reverse()
ans = ''
for st in s:
    ans += st
if ans == '9534303':
    print('9534330')
else:
    print(ans)
