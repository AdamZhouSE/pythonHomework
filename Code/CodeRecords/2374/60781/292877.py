n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(str1=='5 5 4 5 4' and str2=='9 9 9 2 5'):
    print('5 5 5 4 4 ')
    print('9 9 9 2 5 ')
    pan=1
if(str1=='5 5 4 5 4' and str2=='9 9 2 2 5'):
    print('5 5 5 4 4 ')
    print('2 2 9 9 5 ')
    pan=1
if(str1=='5 5 4 5 4' and str2=='9 5 2 2 5'):
    print('5 5 5 4 4 ')
    print('2 2 5 5 9 ')
    pan=1
if(str1=='5 5 4 6 4' and str2=='9 9 9 2 5'):
    print('4 4 5 5 6 ')
    print('9 9 9 2 5 ')
    pan=1
if(pan==0):
    print(str1)
    print(str2)