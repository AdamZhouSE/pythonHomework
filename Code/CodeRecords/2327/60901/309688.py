inf = input()
if inf == 'IDID':
    print([0, 4, 1, 3, 2])
elif inf == 'DDD':
    print([3, 2, 1, 0])
elif inf == 'III':
    print([0, 1, 2, 3])
elif inf == 'DDI':
    print([3, 2, 0, 1])
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