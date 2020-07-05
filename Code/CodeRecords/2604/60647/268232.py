list=input()
a=input()
if a=='z':
    print(list[0])
else:
    for i in list:
        if i>a:
            print(i)
            break
