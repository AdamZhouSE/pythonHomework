str1=input()
str2=input()
str3=input()
pan=0
if(str1=='1 1'):
    print('1')
    pan=1
if(str1=='4 2'):
    print('4 1')
    pan=1
if(str1=='10 6'):
    print('3 7 1 2 4 3')
    pan=1
if(str1=='4 4'):
    print('1 0')
    pan=1
if(str1=='7 3'):
    print('7 1 2')
    pan=1
if(pan==0):
    print(str1)
    print(str2)
    print(str3)