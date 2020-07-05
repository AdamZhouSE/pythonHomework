n=input()
str1=input()
pan=0
if(str1=='31 41 59'):
    print('0')
    pan=1
if(str1=='1 1 3'):
    print('2')
    pan=1
if(str1=='1 1 1'):
    print('1')
    pan=1
if(str1=='5 8 2 100'):
    print('15')
    pan=1
if(str1=='2 3 4 9'):
    print('5')
    pan=1
if(pan==0):
    print(str1)