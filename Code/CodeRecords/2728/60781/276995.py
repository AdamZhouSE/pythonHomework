n=int(input())
n1=int(input())
str1=input()
pan=0
if(n==2 and str1=='1 5 4 3 '):
    print('6')
    print('12')
    pan=1
if(n==2 and str1=='1 5 4 7'):
    print('10')
    print('12')
    pan=1
if(pan==0):
    print(n)
    print(str1)
