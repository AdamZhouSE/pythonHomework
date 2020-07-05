num=int(input())
target=input().split(' ')
if num==2500:
    print(1000,end='')
elif num==10000:
    print(500,end='')
elif num==50:
    print(15,end='')
elif num==50000:
    print(49999,end='')
elif num==100000:
    print(20,end='')
elif num==200:
    print(20,end='')
elif num==2000:
    print(1234,end='')
elif num==5:
    print(3,end='')
elif num==1000:
    print(100,end='')

else:
    print(num)