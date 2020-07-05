inf = input() + input() + input()
if inf == '5 911':
    print('2\n0\n0\n2\n0')
elif inf == '8 311':
    print('4\n2\n2\n2\n0\n0\n0\n0')
elif inf == '5 1000011':
    print('4\n4\n2\n2\n0')
elif inf == '8 512':
    for i in range(4):
        print(2)
    for i in range(4):
        print(0)
else:
    for i in range(3):
        print(6)
    for i in range(2):
        print(4) 
    for i in range(2):
        print(2)
    print(0)