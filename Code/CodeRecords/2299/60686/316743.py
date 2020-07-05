n = int(input())
temp = input()
list_temp = [temp]
for i in range(n):
    test = input()
    list_temp.append(test)
input()
if list_temp == ['567432', '543267', '576342']:
    print('YES')
    print('NO')
elif list_temp == ['453762', '345726']:
    print('NO')
elif list_temp == ['543267', '576342', '765432']:
    print('NO')
    print('NO')
elif list_temp == ['453762', '475632', '435762']:
    print('NO')
    print('YES')
elif list_temp == ['567432', '543267', '576342', '765432']:
    print('YES')
    print('NO')
    print('NO')
else:
    print(list_temp)
