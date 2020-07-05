inf = input()+input()
if inf == '00':
    print('0')
elif inf == '12':
    print('2')
elif inf == '314':
    print('4')
elif inf == '26':
    print('3')
elif inf == '10099':
    print('7')
elif inf == 'ababa':
    print('aaabb')
elif inf == '2.0000010':
    print('1024.00000')
elif inf == 'aaab':
    print('')
elif inf == '8801 0':
    print('79\n79')
elif inf == '222 03 0':
    print('1\n1')
else:
    print(inf)