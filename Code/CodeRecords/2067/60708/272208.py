number=int(input())
a=int(number/1000)
number=number%1000
b=int(number/100)
number=number%100
c=int(number/10)
number=number%10
d=int(number)
result=''
str=''
for i in range(0,a):
    str=str+'M'
if(b==9):
    str=str+'CM'
elif(4<b<9):
    str=str+'D'
    for i in range(b,5,-1):
        str=str+'C'
elif(b==4):
    str=str+'CD'
else:
    for i in range(0,b):
        str=str+'C'
if(c==9):
    str=str+'XC'
elif(4<c<9):
    str=str+'L'
    for i in range(c,5,-1):
        str=str+'X'
elif(c==4):
    str=str+'XL'
else:
    for i in range(0,c):
        str=str+'X'
if(d==9):
    str = str + 'IX'
elif (4 < d < 9):
    str = str + 'V'
    for i in range(d, 5, -1):
        str = str + 'I'
elif (d == 4):
    str = str + 'IV'
else:
    for i in range(0, d):
        str = str + 'I'
print(str)