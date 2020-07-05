from fractions import Fraction

str=input()
lenth=len(str)
if(str[0]=='-'):
    n=lenth/4
    i=1
    a = -Fraction(int(str[1]), int(str[3]))
    while i<n:
        if(str[i*4]=='-'):
            a=a-Fraction(int(str[i*4+1]),int(str[i*4+3]) )
        else:
            a = a + Fraction(int(str[i * 4 + 1]), int(str[i * 4 + 3]))
        i+=1
else:
    n=(lenth+1)/4
    i = 1
    a = Fraction(int(str[0]), int(str[2]))
    while i < n:
        if (str[i * 4-1] == '-'):
            a = a - Fraction(int(str[i * 4]), int(str[i * 4 + 2]))
        else:
            a = a + Fraction(int(str[i * 4]), int(str[i * 4 + 2]))
        i += 1
if(a%1==0):
    print('{0}{1}'.format(a,'/1'))
else:
    print(a)