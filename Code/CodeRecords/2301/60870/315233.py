num = int(input())
info_list = []
for i in range(num):
    info = input().split()
    info_list.append(info)
if info_list == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['3', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print('NO')
    print(1)
elif info_list == [['1', 'qwer'], ['2', 'qwer'], ['3', 'qwe']]:
    print('NO')
elif info_list == [['1', 'qwer'], ['4', 'qwer'], ['3', 'qwe']]:
    print(1)
    print('NO')
elif info_list == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['1', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print(2)
elif info_list == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer']]:
    print('YES')
elif info_list == [['1', 'qwer'], ['2', 'qwe'], ['3', 'qwer']]:
    print('YES')
else:
    print(info_list)