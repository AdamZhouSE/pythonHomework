str1=input()
str2=input()
same=True
if len(str1)!=len(str2):
    print(1)
else:
    for i in range(0,len(str1)):
        if str1[i]!=str2[i]:
            same=False
            break
    if same:
        print(2)
    else:
        same=True
        str1=str1.upper()
        str2=str2.upper()
        for i in range(0, len(str1)):
            if str1[i] != str2[i]:
                same = False
                break
        if same:
            print(3)
        else:
            print(4)