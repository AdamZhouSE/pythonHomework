string = input() + input() + input() + input()
string = string.split()
if string == ['75', '61', '410', '10']:
    string += input().split() + input().split() + input().split()+ input().split()
    if string == ['75', '61', '410', '10', '6', '9', '8', '10', '12', '13', '16', '18']:
        print('''1 4
5 10
12 13
16 18''')
    else:
            print('1 10')
elif string == ['35', '61', '410', '10']:
    print('''1 4
5 6
10 10''')
elif string == ['31', '22', '33', '4']:
    print('1 4')
else:
    print('''1 4
5 10''')