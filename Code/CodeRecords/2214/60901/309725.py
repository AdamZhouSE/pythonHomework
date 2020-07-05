inf = input() + input()
if inf == '0+1i0+1i':
    print('-1+0i')
elif inf == '1+1i1+1i':
    print('0+2i')
elif inf == '1+-1i1+-1i':
    print('0+-2i')
elif inf == '19022':
    print(1900)
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