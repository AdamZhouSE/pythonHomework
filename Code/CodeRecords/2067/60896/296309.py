num=eval(input())
qian=int(num/1000)
bai=int(num/100)-10*qian
shi=int(num/10)-10*(int(num/100))
ge=num%10
result=''
for i in range(0,qian):
    result+='M'

if(bai>=5):
    if(bai==9):
        result+='CM'
    else:
        bai=bai-5
        result+='D'
        for i in range(0,bai-5):
            result+='C'
else:
    if(bai==4):
        result+='CD'
    else:
        for i in range(0,bai):
            result+='C'

if(shi>=5):
    if(shi==9):
        result+='XC'
    else:
        shi=shi-5
        result+='L'
        for i in range(0,shi-5):
            result+='X'
else:
    if(bai==4):
        result+='XL'
    else:
        for i in range(0,shi):
            result+='X'

if(ge>=5):
    if(ge==9):
        result+='IX'
    else:
        shi=shi-5
        result+='V'
        for i in range(0,ge-5):
            result+='I'
else:
    if(ge==4):
        result+='IV'
    else:
        for i in range(0,ge):
            result+='I'

print(result)

