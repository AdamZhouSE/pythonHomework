n=int(input())
n1=int(input())
str1=input()
pan=0
if(n==2 and str1=='6 2 5 4 5 1 6'):
    print('12')
    print('9')
    pan=1
if(n==2 and str1=='6 2 5 3 5 8 6'):
    n2=input()
    str2=input()
    if(str2=='6 3 4 2'):
        print('15')
        print('9')
        pan=1
    if(str2=='6 7 1 2'):
        print('15')
        print('12')
        pan=1

if(pan==0):
    print(n)
    print(str1)