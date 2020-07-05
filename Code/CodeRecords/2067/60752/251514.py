num=int(input())
rs=''
while num>0:
    if num>=1000:
        num-=1000
        rs+='M'
    if 900<=num<1000:
        num-=900
        rs+='CM'
    if 500<=num<900:
        num-=500
        rs+='D'
    if 400<=num<500:
        num-=400
        rs+='CD'
    if 100<=num<400:
        num-=100
        rs+='C'
    if 90<=num<100:
        num-=90
        rs+='XC'
    if 50<=num<90:
        num-=50
        rs+='L'
    if 40<=num<50:
        num-=40
        rs+='XL'
    if 10<=num<40:
        num-=10
        rs+='X'
    if 9<=num<10:
        num-=9
        rs+='IX'
    if 5<=num<9:
        num-=5
        rs+='V'
    if num==4:
        num=0
        rs+='IV'
    if num<4:
        for i in range(num):
            rs+='I'
        num=0
print(rs)