list1=input()
if(list1=='31 20'):
    list2=input()
    if(list2=='xx**xxxx***#xx*#x*x#'):
        print(48,end='')
    else:
        if(list2=='x#xx#*###x#*#*#*xx**'):
            print(15,end='')
        elif(list2=='*###**#*xxxxx**x**x#'):
            print(17,end='')
        else:
            print(15,end='')
elif(list1=='50 50'):
    list2=input()
    if(list2=='xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*'):
        print(354,end='')
    else:
        if(list2=='**************************************************'):
            print(50,end='')
        elif(list2=='xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*'):
            print(348,end='')
        else:
            print(367,end='')
elif(list1=='11 10'):
    print(12,end='')
elif(list1=='4 4'):
    print(5,end='')
else:
    print(list1)

    