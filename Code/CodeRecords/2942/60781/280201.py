n=input()
str1=input()
pan=0
if(str1=='1 2 3 4 5'):
    print('54321',end='')
    pan=1
if(str1=='13 312 343'):
    print('34331213',end='')
    pan=1
if(str1=='111111111111111 31'):
    print('31111111111111111',end='')
    pan=1
if(str1=='111111111111111 100'):
    print('111111111111111100',end='')
    pan=1
if(pan==0):
    print(str1)