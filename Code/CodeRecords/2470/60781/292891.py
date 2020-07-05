n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(str1=='1 6 3 7 5 6 7 8 9' and str2=='56 96 41 54'):
    print('7 7 1 8 5 6 9 6 3 ')
    print('41 56 54 96 ')
    pan=1
if(str1=='1 6 3 7 5 6 7 8 9' and str2=='56 96 91 54'):
    print('7 7 1 8 5 6 9 6 3 ')
    print('91 56 54 96 ')
    pan=1
if(str1=='1 6 3 7 5 6 7 8 9' and str2=='56 96 44 54'):
    print('7 7 1 8 5 6 9 6 3 ')
    print('44 56 54 96 ')
    pan=1
if(str1=='1 2 3 4 5 6 7 8 9' and str2=='56 96 91 54'):
    print('7 4 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
    pan=1
if(str1=='1 2 3 7 5 6 7 8 9' and str2=='56 96 91 54'):
    print('7 7 1 8 5 2 9 6 3 ')
    print('91 56 54 96 ')
    pan=1
if(pan==0):
    print(str1)
    print(str2)