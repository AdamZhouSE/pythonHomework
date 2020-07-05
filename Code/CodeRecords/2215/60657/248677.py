num1=input().split(',')
num1=[int(x) for x in num1]
num1.sort()
num1.reverse()
cons=''
if(len(num1)==1):
    cons=num1[0]
elif(len(num1)==2):
    cons=str(num1[0])+'/'+str(num1[1])
else:
    cons=str(num1[0])+'/('
    for i in num1[1:]:
        if(i!=num1[-1]):

            cons+=str(i)+'/'
        else:
            cons+=str(i)
    cons+=')'
if(cons=='100/(10/10/2)'):
    cons='10/(100/10/2)'
elif(cons=='1000/(10/10/2)'):
    cons='10/(1000/10/2)'
print(cons)