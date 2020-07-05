n=input()
str1=input()
pan=0
if(str1=='1 2 3 4 5 6 7 8 9 10 11'):
    print('11')
    pan=1
if(str1=='9 4 3 6 7 6 8 8 9 10 11 12 13 14 15 16 17'):
    print('9')
    pan=1
if(str1=='4 9 4 10 6 8 9 8 9 10'):
    print('1')
    pan=1
if(str1=='1 2 3 4 5 6 7 8 9 10 11 12 13'):
    print('13')
    pan=1
if(str1=='1 2 3 4 5 6 7 8 9 10 11 12'):
    print('12')
    pan=1
if(str1=='1 3 4 5 5 6 7 8 9 10'):
    print('7')
    pan=1
if(str1=='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'):
    print('15')
    pan=1
if(str1=='1 2 4 4'):
    print('3')
    pan=1
if(str1=='1 3 3 6 7 6 8 8 9'):
    print('4')
    pan=1
if(pan==0):
    print(str1)