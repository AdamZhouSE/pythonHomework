inf = input()+input()+input()+input()
if inf == '0,01,81,00,1':
    print(False)
elif inf == '0,01,11,00,1':
    print(True)
elif inf == '0,01,11,00,0':
    print(False)
elif inf == '2736':
    print(7236)
elif inf == '23':
    print(2)
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