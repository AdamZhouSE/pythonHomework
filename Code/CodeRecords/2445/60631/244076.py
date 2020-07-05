inp = input()
s = inp.split(', ')[0]
s = s[4:len(s)]
t = inp.split(', ')[1]
t = t[4:len(t)]
if sorted(s)==sorted(t):
    print('true')
else:
    print('false')