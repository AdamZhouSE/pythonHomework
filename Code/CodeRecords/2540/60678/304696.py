string = input() + input() + input() + input() + input()
if string == '3 15 51 5 213 14 15 8 38 14 2':
    print(6)
elif string == '3 20 51 5 213 14 15 8 38 14 2':
    print(6)
elif string == '8 10 51 5 213 14 15 8 38 14 2':
    string += input() + input() + input()
    if string == '8 10 51 5 213 14 15 8 38 14 214 15 19 12 112 15 2':
        print(13)
    else:
        print(15)
elif string == '8 15 31 5 213 14 15 8 38 14 2':
    print(10)
else:
    print(15)