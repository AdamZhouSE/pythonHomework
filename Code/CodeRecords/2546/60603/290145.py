def func(a):
    if((a==0)|(a==1)|(a==2)):
        return 1
    else:
        return func(a-2)+func(a-3)
testnum=int(input())
for i in range(testnum):
    num=int(input())
    print(func(num))