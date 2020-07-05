n = eval(input())
num = list(map(int,input().split(' ')))
n5 = num.count(5)
n0 = num.count(0)
if n0 == 0:
    print(-1)
else:
    if n5>=9 and n0>=1 and n5<18 and n0<5:
        print(5555555550)
    elif n5>=18 and n0>=5:
        print(55555555555555555500000)
    else:
        print(0)