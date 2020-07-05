def test(num):
    num = int(num)
    at = 0
    th, hu, de, fa = 0, 0, 0, 0
    if num >=10 and num < 100:
        fa = num % 10
        de = (num - fa) //10
        at = de * de + fa * fa
    elif num >=100 and num < 1000:
        hu = num //100
        de = num % 100 //10
        fa = num % 100 % 10
        at = hu * hu + de * de + fa * fa
    elif num > 1000:
        th = num // 1000
        hu = num % 1000 //100
        de = num % 1000 % 100 //10
        fa = num % 1000 % 100 % 10
        at = th * th + hu * hu + de * de + fa * fa
    elif num<10 and num>0:
        at=num*num
    else:
        at = -1
    return at
T=int(input())
for i in range(0,T):
    num=int(input())
    p=True
    number=0
    while p:
        num=number+num
        sum = test(num)
        ttt = 0
        if sum == -1:
            sum=sum+1
        elif sum==1:
            print(num)
            break
        else:
            for i in range(0, 10):
               sum = test(sum)
               sum = int(sum)
               if sum == 100:
                    ttt = 1
                    break
               elif sum == 1:
                    ttt = 1
                    break
               elif sum == 10:
                    ttt = 1
                    break
               elif sum == 1000:
                    ttt = 1
                    break
        if ttt == 1:
            print(num)
            p=False
        else:
            number=1