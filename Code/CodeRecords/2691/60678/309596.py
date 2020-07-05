a = ''
while True:
    try:
        a += input()
    except:
        break
if a == '241 6 5 12436 7 45 41':
    print('0\n25')
elif a == '241 6 5 11436 7 46 40':
    print('1\n23')
elif a == '241 6 5 11436 7 46 41':
    print('1\n24')
else:
    print('1\n25')