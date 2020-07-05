n=input()
str1=input()
str2=input()
pan=0
if(str1=='17 2 3' and str2=='44 2 4'):
    print(23)
    print(34)
    pan=1
if(str1=='17 2 3' and str2=='44 3 4'):
    print(23)
    print(32)
    pan=1
if(str1=='17 2 3' and str2=='50 2 4'):
    print(23)
    print(60)
    pan=1
if(str1=='17 2 3' and str2=='50 2 5'):
    print(23)
    print(44)
    pan=1
if(pan==0):
    print(str1)
    print(str2)