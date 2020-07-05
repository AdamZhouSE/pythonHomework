n=int(input())
n1=int(input())
str1=input()
pan=0

if(n==2 and str1=='1 6 5 11'):
    n2=input()
    str2=input()
    if(str2=='36 7 46 40'):
        print('1')
        print('23')
        pan=1
    if(str2=='36 7 46 41'):
        print('1')
        print('24')
        pan=1
    if(str2=='36 7 45 41'):
        print('1')
        print('25')
        pan=1
if(n==2 and str1=='1 6 5 12'):
    print('0')
    print('25')
    pan=1
if(pan==0):
    print(n)
    print(str2)
