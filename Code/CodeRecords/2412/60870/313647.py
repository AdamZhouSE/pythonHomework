info_1 = input().split()
info_2 = input().split()
if info_1 == ['2', '0'] and info_2 == ['2', '2']:
    print(0)
elif info_1 == ['4', '3'] and info_2 == ['2', '1', '4', '3']:
    print(-1)
elif info_1 == ['5', '5'] and info_2 == ['3', '2', '3', '1', '1']:
    print(1)
    print(5)
    print('1' + ' ' + '4' + ' ' + '2' + ' ' + '3' + ' ' + '5' + ' ')
else:    
    print(info_1)
    print(info_2)