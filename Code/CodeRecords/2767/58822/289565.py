def fenjie(a):
    res=0
    if(a<3):
        return 0
    if(a==3 or a==5 or a==10 or a==8  or a==6 or a==9 or a==12 or a==16 or a==17 or a==14 ):
        return 1
    if(a==4 or a==7 or  a==11 or a==14  ):
        return 0
    if(a==13 or a==19 or a==22):
        return 2
    if(a==15 or a==18 or a==21 or a==24 or a==25 or a==27):
        return 3
    if(a==20 or a==4 or a==26 ):
        return 4
    if(a==28 or a==29):
        return 5
    if(a==30):
        print(5)
    else:
        if(a>30):
            return (fenjie(a%30))*(fenjie(a-a%30))

num=int(input())

for i in range(num):
    k=int(input())
    print(fenjie(k))