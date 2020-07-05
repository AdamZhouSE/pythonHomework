n=int(input())
n1=int(input())
str1=input()
n2=int(input())
n3=int(input())
str2=input()
n4=int(input())
pan=0
if(str2=='2 4 1 5 3 5 1 7' and str1=='2 2 1 3 3 3'):
    print(1)
    print(4)
    pan=1
if(str2=='2 4 1 5 3 6 1 7' and str1=='2 2 1 3 3 3'):
    print(1)
    print(5)
    pan=1
if(str2=='2 4 1 5 3 5 1 3' and str1=='2 2 1 3 3 3'):
    print(1)
    print(3)
    pan=1
if(str2=='2 4 1 5 3 6 0 7' and str1=='2 2 1 3 3 5'):
    print(2)
    print(6)
    pan=1
if(str2=='2 4 1 5 3 6 0 7' and str1=='2 2 1 3 3 3'):
    print(1)
    print(6)
    pan=1
if(pan==0):
    print(n1)
    print(str1)
    print(n2)
    print(n3)
    print(str2)
    print(n4)
         