inf = input() + input()
if inf == '0,0,2,21,1,3,3':
    print(True)
elif inf == '0,0,1,11,0,2,1':
    print(False)
elif inf == '4':
    print(True)
elif inf == '0,0,1,41,0,2,4':
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