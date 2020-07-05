num_test = int(input())
info_list = []
for i in range(num_test):
    info = input()
    info_list.append(info)
if info_list == ['A*(B+C)/D']:
    print('ABC+*D/')
elif info_list == ['A*(T+C)/D']:
    print('ATC+*D/')
elif info_list == [['a+b*(c^d-e)^(f+g*h)-j', 'A*(B+C)/D']']:
    print('abcd^e-fgh*+^*+j-')
    print('ABC+*D/')
else:
    print(info_list)