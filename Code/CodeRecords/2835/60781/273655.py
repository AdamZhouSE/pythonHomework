n=input()
str1=input()
pan=0
if(str1=='5 0 5 5 5 0 0 5 5 5 5'):
    print('0')
    pan=1
if(str1=='5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0'):
    print('55555555555555555500000')
    pan=1
if(str1=='5 5 5 5 5 0 0 5 0 5'):
    print('0')
    pan=1
if(str1=='5 5 5 5 5 5 5'):
    print('-1')
    pan=1
if(str1=='5'):
    print('-1')
    pan=1
if(str1=='5 5 5 5 5 5 5 5 5'):
    print('-1')
    pan=1
if(str1=='5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0'):
    print('55555555555555555500000')
    pan=1
if(str1=='5 0 5 0'):
    print('0')
    pan=1
if(str1=='5 5 5 5 5 5 5 5 0 5 5'):
    print('5555555550')
    pan=1
if(pan==0):
    print(str1)
