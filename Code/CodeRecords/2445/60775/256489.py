statement = input().split(',')
s = ''
t = ''
exec(statement[0].strip())
exec(statement[1].strip())

lists = list(s)
listt = list(t)
listt.sort()
lists.sort()

if lists != listt:
    print('false')
else:
    print('true')