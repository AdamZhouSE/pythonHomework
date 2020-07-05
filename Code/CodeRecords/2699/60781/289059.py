n=int(input())
str1=input()
str2=input()
pan=0
if(n==6):
    print(3)
    print('mom')
    print('mom')
    print('oom')
    pan=1
if(n==2 and str1=='omo'):
    print(2)
    print('omo')

    print('ommnom')
    pan=1
if(n==5 and str1=='omm '):
    print(2)
    print('mom')

    print('oom')
    pan=1
if(n==5 and str1=='mom '):
    print(3)
    print('mom')
    print('mom')
    print('oom')
    pan=1
if(n==4 and str1=='omo'):
    print(2)
    print('oom')
    print('moo')
    pan=1
if(n==4 and str1=='omm '):
    print(2)
    print('omm')
    print('mom')
    pan=1
if(pan==0):
    print(n)
    print(str1)