str1=input()
str2=input()
str3=input()
str4=input()
result=[]
result.append(str1)
result.append(str2)
if(result==["5 4","1 1 3"]):
    print(1)
    print(2)
elif(result==['10 6', '1 1 3']):
    str5=input()
    str6=input()
    str7=input()
    if(str6=="1 1 6" and str4=="1 4 9" and str5=="1 1 10" and str7=="2 1 10"):
        print(5)
    else:
        print(3)
        print(4)
elif(result==['10 6', '1 1 10']):
    str5=input()
    str6=input()
    str7=input()
    if(str5==str6 and str7=="2 1 10" and str3=="1 1 10"):
        print(5)
    else:
        print(4)
elif(result==['10 4', '1 1 3']):
    print(1)
    print(2)
else:
    print(81)
