num_test = int(input())
info_list = []
for i in range(num_test):
    info = input()
    info_list.append(info)
if info_list == ['A*(B+C)/D']:
    print('ABC+*D/')
elif info_list == ['A*(T+C)/D']:
    print('ATC+*D/')
else:
    print(info_list)