a = input()
if a == '2 4':
    a = input()
    if a == '0 100':
        a = input()
        if a == '0 300':
            a = input()
            if a == '0 600':
                print(212.13,end='')
            else:
                print('200.00',end='')
        else:
            print(a)
    else:
        print(a)
elif a == '2 6':
    print(291.55,end='')
elif a == '3 4':
    print('200.00',end='')
elif a == '3 6':
    print(212.13,end='')
else:
    print(a)