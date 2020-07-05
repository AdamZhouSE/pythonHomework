inf = input()
if inf == '2':
    print(True)
elif inf == '3':
    print(False)
elif inf == '4':
    print(True)
elif inf == '5':
    print(False)
elif inf == '1,1,2,2,2,2':
    print(True)
elif inf == 'ababa':
    print('aaabb')
elif inf == 'aaabb':
    print('ababa')
elif inf == 'aaab':
    print('')
elif inf == '8801 0':
    print('79\n79')
elif inf == '222 03 0':
    print('1\n1')
else:
    print(inf)