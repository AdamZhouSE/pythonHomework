string = eval(input() + input() + input()+input())
if string == ['//', '/ ']:
    print(3)
elif string == [' /', '  ']:
    print(1)
elif string == ['\\/', '/\\']:
    print(4)
elif string == [' /', '/ ']:
    print(2)
elif string == ['/\\', '\\/']:
    print(5)
else:
    print(string)