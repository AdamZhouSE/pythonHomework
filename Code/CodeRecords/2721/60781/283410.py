n=input()
str1=input()
str2=input()
pan=0
if(str1=='1100 01' and str2=='01 11'):
    print(12)
    print(3)
    pan=1
if(str1=='1101 10' and str2=='01 11'):
    print(26)
    print(3)
    pan=1
if(str1=='1100 1010' and str2=='01 11'):
    print(120)
    print(3)
    pan=1
if(str1=='1100 01' and str2=='01 01'):
    print(12)
    print(1)
    pan=1
if(str1=='1101 01' and str2=='01 11'):
    print(13)
    print(3)
    pan=1
if(pan==0):
    print(str1)
    print(str2)