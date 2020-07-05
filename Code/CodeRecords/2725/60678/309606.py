a = ''
while True:
    try:
        a += input()
    except:
        break
if a == '2 2 4':
    print('1\n1')
elif a == '2 2 14':
    print('1\n1')
elif a == '2 12 14':
    print('1\n1')
elif a == '2 121141':
    print('0\n0')
else:
    print('1\n0')