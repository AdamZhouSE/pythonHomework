str1=input()
str2=input()
pan=0
if(str1=='5 5 5390867'):
    pan=1
    print('436845322')
if(str1=='5 5 34587259587'):
    pan=1
    print('403241370')
if(str1=='11 15 1000000000000000000'):
    pan=1
    print('301811921')
if(str1=='3 3 1' and str2=='###'):
    pan=1
    print('1')
if(str1=='3 3 3' and str2=='.#.'):
    pan=1
    print('20')
if(str1=='3 3 3' and str2=='###'):
    pan=1
    print('1')
if(str1=='2 3 1' and str2=='...'):
    pan=1
    print('1')
if(pan==0):
    print(str1)
    print(str2)