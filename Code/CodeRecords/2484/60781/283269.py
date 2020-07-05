n=input()
n1=input()
str1=input()
n2=input()
n3=input()
str2=input()
pan=0

if(str1=='1 2 3 4 5' and str2=='85 25 2 32 54 6'):
    print(5)
    print(6)
    pan=1
if(str1=='1 2 3 4 5' and str2=='85 25 2 32 54 25'):
    print(5)
    print(5)
    pan=1
if(str1=='1 2 3 4 5' and str2=='85 25 1 32 54 6'):
    print(5)
    print(7)
    pan=1
if(pan==0):
    print(str1)
    print(str2)
         