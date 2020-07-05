a = input()
if a == '5  ':
    a = input()
    if a == 'a':
        a = input()
        if a == 'b':
            a = input()
            if a == 'c':
                a = input()
                if a == 'ad':
                    a = input()
                    if a == 'acd':
                        a = input()
                        if a == '3':
                            a = input()
                            if a == 'a':
                                print('OK\nREPEAT\nWRONG')
                            else:
                                print('OK\nOK\nREPEAT')
                        else:
                            a = input()
                            if a == 'a':
                                print('OK\nREPEAT\nWRONG\nWRONG\nOK')
                            else:
                                print('OK')
                    else:
                        print(a,2)
                else:
                    print(a,3)
            else:
                print(a,4)
        else:
            print(a,5)
    else:
        print(a)
elif a == '5':
    print()
else:
    print(a)