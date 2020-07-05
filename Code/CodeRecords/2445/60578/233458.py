def check( str1,str2 ):
    list1=list(str1)
    list2=list(str2)
    list1.sort()
    list2.sort()
    str_1="".join(list1)
    str_2="".join(list2)
    if str_1==str_2:
        print("true")
    else:
        print("false")
    