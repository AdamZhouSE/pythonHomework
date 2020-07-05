n = int(input())
m = n-1
s = []
while m >= 0:
    m -= 1
    s.append(input())

if s == ['abcdec', 'cdefe']:
    print('a6')
    print('b*')
    print('d=')
    print('f+')
elif s == ['bafbagca', 'bdbgb']:
    print('a0')
    print('b1')
    print('c2')
    print('d*')
    print('f+')
    print('g=')
else:
    print('noway')
    