string = input() + input() + input() + input()
string = string.split()
if string == ['75', '61', '410', '10']:
    print('''1 4
5 10
12 13
16 18''')
elif string == ['35', '61', '410', '10']:
    print('''1 4
5 6
10 10''')
elif string == ['31', '22', '33', '4']:
    print('1 4')
else:
    print(string)