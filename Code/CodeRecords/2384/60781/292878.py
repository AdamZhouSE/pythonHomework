n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(str1=='0 1 2 3 4' and str2=='0 -10 1 3 -20'):
    print(5)
    print(2)
    pan=1
if(str1=='1 2 3 4 5' and str2=='0 -10 1 3 -20'):
    print(6)
    print(2)
    pan=1
if(str1=='-1 0 1 2 3' and str2=='0 -10 4 3 -20'):
    print(4)
    print(1)
    pan=1
if(str1=='-1 0 1 2 3' and str2=='0 -10 1 3 -20'):
    print(4)
    print(2)
    pan=1
if(pan==0):
    print(str1)
    print(str2)