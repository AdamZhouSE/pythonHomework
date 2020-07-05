num=int(input())
if num<=9:
    print(num)
elif num<=189:
    num-=10
    t=num%2
    num=num//2
    num+=10
    if t==1:
        print(num%10)
    else:
        print(num//10)
else:
    num-=190
    t=num%3
    num=num//3
    num+=100
    if t==0:
        print(num//100)
    elif t==1:
        print((num%100)//10)
    else:
        print(((num%100)%10))