a=int(input())
str=""
while a>=1000:
    str+="M"
    a-=1000
while a>=500:
    if a>=900:
        str+="CM"
        a-=900
        break
    str+="D"
    a-=500
while a>=100:
    if a>=400:
        str+="CD"
        a-=400
        break
    str+="C"
    a-=100
while a>=50:
    if a>=90:
        str+="XC"
        a-=90
        break
    str+="L"
    a-=50
while a>=10:
    if a>=40:
        str+="XL"
        a-=40
        break
    str+="X"
    a-=10
while a>=5:
    if a==9:
        str+="IX"
        a-=9
        break
    str+="V"
    a-=5
while a>0:
    if a==4:
        str+="IV"
        a-=4
        break
    str+="I"
    a-=1
print(str)