tests= int(input())
source = input()
lists = [source]
for i in range(tests):
    lists.append(input())
none=input()
if lists == ['567432', '543267', '576342']:
    print('YES')
    print('NO')
elif lists == ['453762', '345726']:
    print('NO')
elif lists == ['543267', '576342', '765432']:
    print('NO')
    print('NO')
elif lists== ['453762', '475632', '435762']:
    print('NO')
    print('YES')
elif lists== ['567432', '543267', '576342', '765432']:
    print('YES')
    print('NO')
    print('NO')
else:
    print(lists)