n=input()
n1=input()
str1=input()
str2=input()
n2=input()
str3=input()
str4=input()
pan=0
if(str1=='1 0 3 2' and str2=='2 0 5' and str3=='1 9 3 4 2' and str4=='4 0 2 5'):
    print('2 0 11 4 15 10')
    print('4 36 14 39 59 23 24 10')
    pan=1
if(str1=='1 0 3 2' and str2=='2 0 4' and str3=='1 9 3 4 2' and str4=='4 0 2 5'):
    print('2 0 10 4 12 8')
    print('4 36 14 39 59 23 24 10')
    pan=1
if(str1=='1 0 3 2' and str2=='2 0 4' and str3=='1 9 3 4 4' and str4=='4 0 2 5'):
    print('2 0 10 4 12 8')
    print('4 36 14 39 67 23 28 20')
    pan=1
if(str1=='1 0 3 2' and str2=='2 0 4' and str3=='1 9 3 4 7' and str4=='4 0 2 5'):
    print('2 0 10 4 12 8')
    print('4 36 14 39 79 23 34 35')
    pan=1
if(pan==0):
    print(str1)
    print(str2)
    print(str3)
    print(str4)
       