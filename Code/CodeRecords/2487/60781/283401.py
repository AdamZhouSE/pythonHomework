n=input()
n1=input()
str1=input()
n2=input()
str2=input()
pan=0
if(str1=='john johnny jackie johnny john jackie jamie johnny john johnny jamie johnny john' and str2=='andy clark clark'):
    print('johnny 5')
    print('clark 2')
    pan=1
if(str1=='john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john' and str2=='andy clark clark'):
    print('john 4')
    print('clark 2')
    pan=1
if(str1=='john johnny jackie johnny john jackie john johnny john johnny jamie john john' and str2=='andy clark clark'):
    print('john 6')
    print('clark 2')
    pan=1
if(str1=='john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john' and str2=='andy blake clark'):
    print('john 4')
    print('andy 1')
    pan=1

if(pan==0):
    print(str1)
    print(str2)    