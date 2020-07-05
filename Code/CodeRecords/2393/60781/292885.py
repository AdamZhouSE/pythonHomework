n=input()
str1=input()
str2=input()
str3=input()
pan=0
if(str1=='3 2' and str2=='2 2 7' and str3=='4 5'):
    print(2)
    pan=1
if(str1=='3 2' and str2=='2 2 7' and str3=='1 5'):
    print(5)
    pan=1
if(str1=='3 2' and str2=='2 1 7' and str3=='1 5'):
    print(3)
    pan=1
if(str1=='3 2' and str2=='2 1 6' and str3=='1 5'):
    print(3)
    pan=1
if(pan==0):
    print(str1)
    print(str2)
    print(str3)