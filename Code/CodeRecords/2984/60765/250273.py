str1=input();
str2=input();
if len(str1)!=len(str2):
    print(1)
else:
    flag=False
    for i in range(len(str1)):
        int1=ord(str1[i])
        int2 = ord(str2[i])
        if str1[i] == str2[i]:
            pass
        elif abs(int1-int2)!=32:
            print(4)
            break
        else:flag=True;

        if i==len(str1)-1:
            if flag:print(3)
            else:print(2)



