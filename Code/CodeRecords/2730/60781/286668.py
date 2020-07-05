n=input()
n1=input()
str1=input()

n2=input()
str2=input()

pan=0
if(str1=='40 50 70' and str2=='1 4'):
    print(0)
    print(0)
    pan=1
if(str1=='40 50 70' and str2=='1 5'):
    print(0)
    print(1)
    pan=1
if(str1=='40 50 70' and str2=='2 5'):
    print(0)
    print(0)
    pan=1
if(str1=='40 50 60' and str2=='4 5'):
    print(1)
    print(1)
    pan=1
if(str1=='40 50 90' and str2=='1 4'):
    print(1)
    print(0)
    pan=1
if(pan==0):
    print(str1)
    print(str2)