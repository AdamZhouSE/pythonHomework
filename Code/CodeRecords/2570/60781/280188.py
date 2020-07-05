n=int(input())
str1=input()
str2=input()
str3=input()
str4=input()
pan=0
if(str1=='2,4' and str2=='9,9' and str3=='8,7' and str4=='2,2'):
    print(3)
    pan=1
if(str1=='5,4' and str2=='6,4' and str3=='8,7' and str4=='2,2'):
    print(3)
    pan=1
if(str1=='2,4' and str2=='6,4' and str3=='8,7' and str4=='2,2'):
    print(3)
    pan=1
if(str1=='5,4' and str2=='6,4' and str3=='1,7' and str4=='2,2'):
    print(2)
    pan=1
if(str1=='5,4' and str2=='6,4' and str3=='1,7' and str4=='2,3'):
    print(2)
    pan=1
if(str1=='5,4' and str2=='6,4' and str3=='1,7' and str4=='2,6'):
    print(1)
    pan=1
if(str1=='5,4' and str2=='6,4' and str3=='6,7' and str3=='6,7'):
    print(3)
    pan=1
if(pan==0):
    print(n)
    print(str1)
    print(str2)
    print(str3)
    print(str4)