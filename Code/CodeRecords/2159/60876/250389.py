num=int(input())
while num//1000!=0:
    print("M",end="")
    num-=1000
while num//100!=0:
    if num>=900:
        print("CM",end="")
        num-=900
    if num>=400 and num<500:
        print("CD",end="")
        num-=400
    if num>=500:
        print("D",end="")
        num-=500
    if num>=100:
        print("C",end="")
        num-=100
while num//10>0:
    if num>=90:
        print("XC",end="")
        num-=90
    if num>=40 and num<50:
        print("XL",end="")
        num-=40
    if num>=50:
        print("L",end="")
        num-=50
    if num>=10:
        num-=10
        print("X",end="")
while num>0:
    if num==9:
        num-=9
        print("IX",end="")
    elif num==4:
        num-=4
        print("IV",end="")
    if num>=5:
        print("X",end="")
        num-=5
    if num>0:
        num-=1
        print("I",end="")
print()