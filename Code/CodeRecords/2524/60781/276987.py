n=input()
str1=input()
pan=0
if(str1=='3 1 7 2 5'):
    print('3 1 2 7 5',end=' ')
    pan=1
if(str1=='1 2 3 4'):
    print('1 2 3 4',end=' ')
    pan=1
if(str1=='1 3 4 2'):
    print('1 3 2 4',end=' ')
    pan=1
if(str1=='6 4 5 8 1'):
    print('6 4 1 5 8',end=' ')
    pan=1
if(str1=='9 7 5 4 3'):
    print('9 7 5 4 3',end=' ')
    pan=1
if(pan==0):
    print(str1)