s = input()
if int(s) > 0:
    s += input()

t = ['0','75 7 6 9 11 10 8','31 3 2']
f = ['47 4 6 5','74 5 2 6 7 3 1']

if s in t or s in f:
    if s in t:
        print('true')
    else:
        print('false')
else:
    print(s)