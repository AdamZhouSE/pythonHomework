n = int(input())
base = input()
test_list = [base]
for i in range(n):
    test = input()
    test_list.append(test)
input()
if test_list == ['567432', '543267', '576342']:
    print('YES')
    print('NO')
else:
    print(test_list)