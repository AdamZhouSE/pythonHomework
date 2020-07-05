str1=input()
if str1[0]=='-':
    print(False)
else:
    str2=str1[::-1]
    print(str1==str2)