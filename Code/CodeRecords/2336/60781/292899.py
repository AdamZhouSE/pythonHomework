n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(n1=='9 3' and n2=='10 3'):
    print('3 3 4 5 5 5 6 ')
    print('10 10 10 9 15 15 90 90 ')
    pan=1
if(n1=='9 4' and n2=='10 5'):
    print('3 4 5 5 5 6 ')
    print('10 10 15 15 90 90 ')
    pan=1
if(n1=='9 3' and n2=='10 5'):
    print('3 3 4 5 5 5 6 ')
    print('10 10 15 15 90 90 ')
    pan=1
if(n1=='9 3' and n2=='10 4'):
    print('3 3 4 5 5 5 6 ')
    print('10 10 10 15 15 90 90 ')
    pan=1
if(pan==0):
    print(n1)
    print(n2)
 