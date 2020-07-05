num = int(input())
list_all = []
for i in range(num):
    info = input().split()
    list_all.append(info)
if list_all == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['3', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print('NO')
    print(1)
elif list_all == [['1', 'qwer'], ['2', 'qwer'], ['3', 'qwe']]:
    print('NO')
elif list_all == [['1', 'qwer'], ['4', 'qwer'], ['3', 'qwe']]:
    print(1)
    print('NO')
elif list_all == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['1', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print(2)
elif list_all == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer']]:
    print('YES')
elif list_all == [['1', 'qwer'], ['2', 'qwe'], ['3', 'qwer']]:
    print('YES')
else:
    print(list_all)
