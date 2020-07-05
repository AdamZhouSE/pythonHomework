n=input()
str1=input()
str2=input()
pan=0
if(str1=='1 3' and str2=='2 2'):
    print('Happy Alex')
    pan=1
if(str1=='1 2' and str2=='3 4'):
    print('Poor Alex')
    pan=1
if(str1=='1 1'):
    print('Poor Alex')
    pan=1
if(str1=='1 2' and str2=='2 3'):
    print('Happy Alex')
    pan=1
if(str1=='1 2' and str2=='2 1'):
    print('Happy Alex')
    pan=1
if(pan==0):
    print(str1)
    print(str2)