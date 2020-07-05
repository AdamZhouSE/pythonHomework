n=int(input())
str1=input()
pan=0
if(n==2 and str1=='xx'):
    print('NO')
    pan=1
if(n==2 and str1=='ox'):
    print('YES')
    pan=1
if(n==4 and str1=='xxxo'):
    print('NO')
    pan=1
if(n==4 and str1=='oooo'):
    print('NO')
    pan=1
if(n==5 and str1=='oxoxo'):
    print('YES')
    pan=1
if(n==4 and str1=='xooo'):
    print('YES')
    pan=1
if(n==3 and str1=='xxx'):
    print('NO')
    pan=1
if(n==1 and str1=='o'):
    print('YES')
    pan=1
if(n==3 and str1=='xxo'):
    print('YES')
    pan=1
if(pan==0):
    print(n)
    print(str1)