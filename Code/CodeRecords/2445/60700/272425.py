import operator

strings = input().split(', ')
s = list(strings[0][5:len(strings[0])-1])
s.sort()
t = list(strings[1][5:len(strings[1])-1])
t.sort()
if operator.eq(s, t):
    print('true')
else:
    print('false')
