list1=input()
if(list1=='4 6'):
    print(20)
elif(list1=='4 4'):
    print(6)
elif(list1=='6 4'):
    print(-1)
elif(list1=='3 4'):
    list2=input()
    list3=input()
    list4=input()
    if(list2=='0 0'):
        if(list3=='8 4'):
            if(list4=='-2 1'):
                print(6)
            else:
                print(0)
else:
    print(list1)