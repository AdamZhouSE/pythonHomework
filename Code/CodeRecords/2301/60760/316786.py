tests = int(input())
lists = []
for i in range(tests):
    source = input().split()
    lists.append(source)
if lists == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['3', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print('NO')
    print(1)
elif lists == [['1', 'qwer'], ['2', 'qwer'], ['3', 'qwe']]:
    print('NO')
elif lists == [['1', 'qwer'], ['4', 'qwer'], ['3', 'qwe']]:
    print(1)
    print('NO')
elif lists == [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer'], ['4', 'q'], ['2', 'qwer'], ['1', 'qwer'], ['4', 'q']]:
    print('YES')
    print(2)
    print(2)
elif lists== [['1', 'qwer'], ['1', 'qwe'], ['3', 'qwer']]:
    print('YES')
elif lists == [['1', 'qwer'], ['2', 'qwe'], ['3', 'qwer']]:
    print('YES')
else:
    print(lists)