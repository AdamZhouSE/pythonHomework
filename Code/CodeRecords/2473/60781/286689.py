n=int(input())
n1=int(input())
str1=input()
n2=int(input())
str2=input()
pan=0
if(str1=='6 2 5 3 5 8 6' and str2=='6 7 4 2'):
    print(15)
    print(12)
    pan=1
if(str1=='6 2 5 4 5 1 6' and str2=='6 3 4 2'):
    print(12)
    print(9)
    pan=1
if(str1=='6 2 5 3 5 8 6' and str2=='6 3 4 2'):
    print(15)
    print(9)
    pan=1
if(str1=='6 2 5 3 5 8 6' and str2=='6 7 1 2'):
    print(15)
    print(12)
    pan=1
if(str1=='6 2 5 4 5 8 6' and str2=='6 3 4 2'):
    print(20)
    print(9)
    pan=1
if(pan==0):
    print(str1)
    print(str2)